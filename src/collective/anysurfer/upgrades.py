# -*- coding: utf-8 -*-
from collective.anysurfer import get_default_text_translations
from collective.anysurfer.interfaces import IAnysurferSettings
from plone import api


def udpate_default_template(context):
    text = get_default_text_translations(api.portal.get())
    api.portal.set_registry_record("text", text, interface=IAnysurferSettings)


def add_control_panel(context):
    context.runImportStepFromProfile(
        "profile-collective.anysurfer:default", "controlpanel"
    )
