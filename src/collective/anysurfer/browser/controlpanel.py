# -*- coding: utf-8 -*-
from collective.anysurfer import _
from collective.anysurfer.interfaces import IAnysurferSettings
from plone.app.registry.browser import controlpanel


class AnysurferSettingsEditForm(controlpanel.RegistryEditForm):
    """Control panel edit form."""

    schema = IAnysurferSettings
    label = _(u"Accessibility (Anysurfer) settings")
    description = _(u"Change all the settings related to website accessibility")

    def updateFields(self):
        super(AnysurferSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(AnysurferSettingsEditForm, self).updateWidgets()


class AnysurferSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    """Control panel form wrapper."""

    form = AnysurferSettingsEditForm
