# -*- coding: utf-8 -*-
from collective.anysurfer import get_default_text
from collective.anysurfer.interfaces import IAnysurferSettings
from plone import api
from plone.app.upgrade.utils import loadMigrationProfile


def udpate_default_template(context):
    text = get_default_text(api.portal.get())
    api.portal.set_registry_record('text', text, interface=IAnysurferSettings)


def reload_gs_profile(context):
    loadMigrationProfile(
        context,
        'profile-collective.anysurfer:default',
    )
