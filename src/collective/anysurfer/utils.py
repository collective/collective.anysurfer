# -*- coding: utf-8 -*-
from plone import api
from plone.app.textfield.value import RichTextValue
from Products.PortalTransforms.libtransforms.utils import bodyfinder


def get_langs():
    language_tool = api.portal.get_tool("portal_languages")
    langs = language_tool.supported_langs
    return langs


def get_default_text_translations():
    """
    Text get from a browser view template <body> tag
    """
    portal = api.portal.get()
    view_name = "default_accessibility_text"
    request = getattr(portal, "REQUEST", None)
    texts = []
    if request is not None:
        for language in get_langs():
            text_translation = {}
            request["LANGUAGE"] = language
            view = api.content.get_view(name=view_name, context=portal, request=request)
            if view is not None:
                text = bodyfinder(view.index()).strip()
                if not isinstance(text, unicode):
                    text = text.decode("utf-8")
                text_translation["language"] = language.decode("utf-8")
                text_translation["text"] = RichTextValue(text, "text/html", "text/html")
                texts.append(text_translation)
    return texts
