# -*- coding: utf-8 -*-
from plone import api
from zope.i18nmessageid import MessageFactory


HAS_PLONE_5 = api.env.plone_version().startswith("5")
HAS_PLONE_6 = api.env.plone_version().startswith("6")
_ = MessageFactory("collective.anysurfer")


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
