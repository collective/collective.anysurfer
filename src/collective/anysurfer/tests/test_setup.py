import unittest2 as unittest
from collective.anysurfer.testing import COLLECTIVE_ANYSURFER_INTEGRATION_TESTING
from plone import api
try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):

    layer = COLLECTIVE_ANYSURFER_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer["app"]
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product
            installed
        """
        self.assertTrue(self.installer.isProductInstalled("collective.anysurfer"))

    def test_default_text_translations(self):
        """ Validate that text is (force) translated during the setup process
        """
        texts = api.portal.get_registry_record(
            "collective.anysurfer.interfaces.IAnysurferSettings.accessibility_translations"
        )
        self.assertEqual(len(texts), 2)
        self.assertNotEqual(texts[0]["text"].output, texts[1]["text"].output)
