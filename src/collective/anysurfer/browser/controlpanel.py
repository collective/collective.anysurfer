from collective.anysurfer import _
from collective.anysurfer.interfaces import IAnysurferSettings
from plone.app.registry.browser import controlpanel


class AnysurferSettingsEditForm(controlpanel.RegistryEditForm):
    """Control panel edit form."""

    schema = IAnysurferSettings
    label = _("Accessibility (Anysurfer) settings")
    description = _("Change all the settings related to website accessibility")

    def updateFields(self):
        super().updateFields()

    def updateWidgets(self):
        super().updateWidgets()


class AnysurferSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    """Control panel form wrapper."""

    form = AnysurferSettingsEditForm
