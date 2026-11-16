from collective.anysurfer.interfaces import ILayerSpecific
from collective.anysurfer.testing import COLLECTIVE_ANYSURFER_INTEGRATION_TESTING
from plone import api
from plone.app.contenttypes.interfaces import IPloneAppContenttypesLayer
from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.testing.zope import Browser
from urllib.error import HTTPError
from zope.interface import alsoProvides

import unittest


class TestTitles(unittest.TestCase):

    layer = COLLECTIVE_ANYSURFER_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer["app"]
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        # Integration tests don't traverse: set the browser layers by hand
        alsoProvides(self.request, ILayerSpecific, IPloneAppContenttypesLayer)

    def asserTitle(self, view_name, title):
        physical_path = list(self.portal.getPhysicalPath())
        physical_path.append(view_name)
        url = "/".join(physical_path)
        full_url = "/".join([self.portal.absolute_url(), view_name])
        self.request.set("URL", full_url)
        self.request.set("ACTUAL_URL", full_url)
        page = self.portal.unrestrictedTraverse(url)()
        return self.assertIn(f"<title>{title}</title>", page)

    def test_contact_title(self):
        browser = Browser(self.app)
        browser.open(f"{self.portal.absolute_url()}/contact-info")
        self.assertEqual(browser.title, "Formulaire de contact — Plone site")

    def test_accessibbility_title(self):
        browser = Browser(self.app)
        browser.open(f"{self.portal.absolute_url()}/accessibility-info")
        self.assertEqual(browser.title, "Accessibilité — Plone site")

    def test_sitemap_title(self):
        browser = Browser(self.app)
        browser.open(f"{self.portal.absolute_url()}/sitemap")
        self.assertEqual(browser.title, "Plan du site — Plone site")

    def test_search_title(self):
        browser = Browser(self.app)
        browser.open(f"{self.portal.absolute_url()}/search")
        self.assertEqual(browser.title, "0 Résultats de recherche — Plone site")

    def test_404_title(self):
        browser = Browser(self.app)
        browser.addHeader("Accept", "text/html")
        try:
            browser.open(f"{self.portal.absolute_url()}/notexisting")
        except HTTPError as e:
            error = e
        self.assertEqual(error.code, 404)
        self.assertEqual(browser.title, "Page non trouvée — Plone site")

    def test_title_without_nav_root(self):
        self.asserTitle("", "Plone site")
        folder = api.content.create(
            type="Folder", container=self.portal, id="folder", title="Folder"
        )
        self.asserTitle("folder", "Folder &mdash; Plone site")
        api.content.create(
            type="Folder", container=folder, id="subfolder", title="Subfolder"
        )
        self.asserTitle("folder/subfolder", "Subfolder &mdash; Plone site")

    def test_title_with_nav_root(self):
        navroot = api.content.create(
            type="Folder", container=self.portal, id="navroot", title="Navroot"
        )
        api.content.create(
            type="Folder", container=navroot, id="subfolder", title="Subfolder"
        )
        alsoProvides(navroot, INavigationRoot)
        self.asserTitle("navroot", "Navroot")
        self.asserTitle("navroot/subfolder", "Subfolder &mdash; Navroot")
