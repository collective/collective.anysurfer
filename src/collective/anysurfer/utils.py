# -*- coding: utf-8 -*-
import six

from collective.anysurfer import HAS_PLONE_5
from plone import api
from plone.registry.interfaces import IRegistry
from plone.app.textfield.value import RichTextValue
from Products.PortalTransforms.libtransforms.utils import bodyfinder
from zope.annotation.interfaces import IAnnotations
from zope.component import getUtility

if HAS_PLONE_5:
    from plone.i18n.utility import setLanguageBinding
    from Products.CMFPlone.interfaces import ILanguageSchema


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
    if request is None:
        return
    texts = []
    if HAS_PLONE_5:
        registry = getUtility(IRegistry)
        language_settings = registry.forInterface(ILanguageSchema, prefix='plone')
        store_cookie_negotiation = language_settings.use_cookie_negotiation
        language_settings.use_cookie_negotiation = True
    else:
        language_tool = api.portal.get_tool("portal_languages")
        store_cookie_negotiation = language_tool.use_cookie_negotiation
        language_tool.use_cookie_negotiation = True

    for language in get_langs():
        text_translation = {}
        # Force language into request
        request["set_language"] = language
        if HAS_PLONE_5:
            setLanguageBinding(request)
        else:
            language_tool.setLanguageBindings()
        view = api.content.get_view(name=view_name, context=portal, request=request)
        if view is not None:
            text = bodyfinder(view.index()).strip()
            if six.PY2:
                text_translation["language"] = language.decode("utf8")
            else:
                text_translation["language"] = language
            text_translation["text"] = RichTextValue(text, "text/html", "text/html")
            texts.append(text_translation)
        if not HAS_PLONE_5:
            IAnnotations(request).clear()
    if HAS_PLONE_5:
        language_settings.use_cookie_negotiation = store_cookie_negotiation
    else:
        language_tool.use_cookie_negotiation = store_cookie_negotiation
    del request.other['set_language']
    return texts
