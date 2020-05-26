# -*- coding: utf-8 -*-
from plone import api
from Products.PortalTransforms.libtransforms.utils import bodyfinder
from zope.i18nmessageid import MessageFactory
from zope.interface import provider
from zope.schema.interfaces import IContextAwareDefaultFactory

_ = MessageFactory("collective.anysurfer")
IS_PLONE4 = api.env.plone_version().startswith("4.3")


def initialize(context):
    """Initializer called when used as a Zope 2 product."""


@provider(IContextAwareDefaultFactory)
def get_default_text(context):
    """
    Text get from a browser view template <body> tag
    """
    portal = api.portal.get()
    view_name = "default_accessibility_text"
    request = getattr(portal, "REQUEST", None)
    if request is not None:
        view = api.content.get_view(name=view_name, context=portal, request=request)
        if view is not None:
            text = bodyfinder(view.index()).strip()
            if not isinstance(text, unicode):
                text = text.decode("utf-8")
            return text
    return u""
