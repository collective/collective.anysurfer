# -*- coding: utf-8 -*-

PROFILE_ID = u"profile-collective.anysurfer:default"


def update_registry(context):
    context.runImportStepFromProfile(PROFILE_ID, "plone.app.registry")


def add_control_panel(context):
    context.runImportStepFromProfile(PROFILE_ID, "controlpanel")
