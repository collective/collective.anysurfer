# -*- coding: utf-8 -*-
from collective.anysurfer.interfaces import ILayerSpecific
from collective.anysurfer.testing import COLLECTIVE_ANYSURFER_INTEGRATION_TESTING
from plone.testing.z2 import Browser
from six.moves.urllib.error import HTTPError
from zope.interface import directlyProvides
import unittest2 as unittest


class TestTitles(unittest.TestCase):

    layer = COLLECTIVE_ANYSURFER_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer["app"]
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        directlyProvides(self.request, ILayerSpecific)

    def asserTitle(self, view_name, title):
        physical_path = list(self.portal.getPhysicalPath())
        physical_path.append(view_name)
        url = "/".join(physical_path)
        self.request.set("URL", url)
        self.request.set("ACTUAL_URL", url)
        page = self.portal.unrestrictedTraverse(url)()
        return self.assertIn("<title>{}</title>".format(title), page)

    def test_contact_title(self):
        self.asserTitle("contact-info", "Contact information &mdash; Plone site")
        browser = Browser(self.app)
        browser.open("{}/contact-info".format(self.portal.absolute_url()))
        self.assertEqual(browser.title, "Formulaire de contact — Plone site")

    def test_accessibbility_title(self):
        self.asserTitle("accessibility-info", "Accessibility &mdash; Plone site")
        browser = Browser(self.app)
        browser.open("{}/accessibility-info".format(self.portal.absolute_url()))
        self.assertEqual(browser.title, "Accessibilit\xc3\xa9 \xe2\x80\x94 Plone site")

    def test_sitemap_title(self):
        self.asserTitle("sitemap", "Site map &mdash; Plone site")
        browser = Browser(self.app)
        browser.open("{}/sitemap".format(self.portal.absolute_url()))
        self.assertEqual(browser.title, "Plan du site \xe2\x80\x94 Plone site")

    def test_search_title(self):
        self.asserTitle("search", "0 Search results &mdash; Plone site")
        browser = Browser(self.app)
        browser.open("{}/search".format(self.portal.absolute_url()))
        self.assertEqual(browser.title, "0 Résultats de recherche — Plone site")

    def test_404_title(self):
        browser = Browser(self.app)
        try:
            browser.open("{}/notexisting".format(self.portal.absolute_url()))
        except HTTPError as e:
            error = e
        self.assertEqual(error.code, 404)
        self.assertEqual(
            browser.title, "Page non trouv\xc3\xa9e \xe2\x80\x94 Plone site"
        )
