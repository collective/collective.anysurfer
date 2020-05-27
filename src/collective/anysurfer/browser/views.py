# -*- coding: utf-8 -*-
from plone import api
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class DefaultPage(BrowserView):

    index = ViewPageTemplateFile("default_accessibility_text.pt")


class AccessibilityView(BrowserView):

    def content(self):
        lang = api.portal.get_current_language()
        accessibility_translations = api.portal.get_registry_record(
            "collective.anysurfer.interfaces.IAnysurferSettings.accessibility_translations",
        )
        for accessibility_translation in accessibility_translations:
            if lang == accessibility_translation.get("language"):
                return accessibility_translation.get("text")
        return u""
