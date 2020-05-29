# -*- coding: utf-8 -*-
from plone import api
from plone.app.textfield.value import RichTextValue
from Products.PortalTransforms.libtransforms.utils import bodyfinder
from zope.annotation.interfaces import IAnnotations


def get_langs():
    language_tool = api.portal.get_tool("portal_languages")
    langs = language_tool.supported_langs
    return langs


def get_default_text_translations():
    """
    Text get from a browser view template <body> tag
    Translation is done by using request-aware language_tool
    """
    portal = api.portal.get()
    view_name = "default_accessibility_text"
    request = getattr(portal, "REQUEST", None)
    texts = []
    language_tool = api.portal.get_tool("portal_languages")
    store_request_negotiation = language_tool.use_request_negotiation
    language_tool.use_request_negotiation = True
    if request is not None:
        for language in get_langs():
            text_translation = {}
            # Force language into request
            request["HTTP_ACCEPT_LANGUAGE"] = language
            language_tool.setLanguageBindings()
            view = api.content.get_view(name=view_name, context=portal, request=request)
            if view is not None:
                text = bodyfinder(view.index()).strip()
                if not isinstance(text, unicode):
                    text = text.decode("utf-8")
                text_translation["language"] = language.decode("utf-8")
                text_translation["text"] = RichTextValue(text, "text/html", "text/html")
                texts.append(text_translation)
            # Clear language negociation cache
            IAnnotations(request).clear()
    language_tool.use_request_negotiation = store_request_negotiation
    language_tool.setLanguageBindings()
    return texts
