# -*- coding: utf-8 -*-
from plone import api
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class DefaultPage(BrowserView):

    index = ViewPageTemplateFile("default_accessibility_text.pt")


class AccessibilityView(BrowserView):

    def content(self):
        text = api.portal.get_registry_record(
            "collective.anysurfer.interfaces.IAnysurferSettings.text", default="",
        )
        return text
