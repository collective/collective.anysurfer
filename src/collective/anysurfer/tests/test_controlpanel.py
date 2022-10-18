# -*- coding: utf-8 -*-
from collective.anysurfer.testing import COLLECTIVE_ANYSURFER_INTEGRATION_TESTING
from plone.app.testing import TEST_USER_ID, applyProfile, setRoles

import unittest


class TestControlPanel(unittest.TestCase):
    """Test control panel."""

    layer = COLLECTIVE_ANYSURFER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]

    def test_configlet_permission(self):
        permission = "collective.anysurfer: Manage control panel"
        roles = self.portal.rolesOfPermission(permission)
        roles = [r["name"] for r in roles if r["selected"]]
        expected = ["Manager", "Site Administrator"]
        self.assertListEqual(roles, expected)
