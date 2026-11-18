from plone import api
from plone.app.textfield.value import RichTextValue
from plone.i18n.interfaces import ILanguageSchema
from plone.i18n.utility import setLanguageBinding
from plone.registry.interfaces import IRegistry
from Products.PortalTransforms.libtransforms.utils import bodyfinder
from zope.component import getUtility


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
    registry = getUtility(IRegistry)
    language_settings = registry.forInterface(ILanguageSchema, prefix="plone")
    store_cookie_negotiation = language_settings.use_cookie_negotiation
    language_settings.use_cookie_negotiation = True

    for language in get_langs():
        text_translation = {}
        # Force language into request
        request["set_language"] = language
        setLanguageBinding(request)
        view = api.content.get_view(name=view_name, context=portal, request=request)
        if view is not None:
            text = bodyfinder(view.index()).strip()
            text_translation["language"] = language
            text_translation["text"] = RichTextValue(text, "text/html", "text/html")
            texts.append(text_translation)
    language_settings.use_cookie_negotiation = store_cookie_negotiation
    del request.other["set_language"]
    return texts
