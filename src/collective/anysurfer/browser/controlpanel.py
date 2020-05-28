# -*- coding: utf-8 -*-
from collective.anysurfer import _
from collective.anysurfer.interfaces import IAnysurferSettings
from plone.app.registry.browser import controlpanel
# from plone.app.textfield.value import RichTextValue
# from plone.app.z3cform.wysiwyg.widget import IWysiwygWidget
# from z3c.form import converter

# import zope.component


class AnysurferSettingsEditForm(controlpanel.RegistryEditForm):
    """Control panel edit form."""

    schema = IAnysurferSettings
    label = _(u'Accessibility (Anysurfer) settings')
    description = _(u'Change all the settings related to website accessibility')

    def updateFields(self):
        super(AnysurferSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(AnysurferSettingsEditForm, self).updateWidgets()


class AnysurferSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    """Control panel form wrapper."""
    form = AnysurferSettingsEditForm


# class RichtextDataConverter(converter.FieldDataConverter):
#     zope.component.adapts(zope.schema.interfaces.IText, IWysiwygWidget)
#
#     def toWidgetValue(self, value):
#         return RichTextValue(value, 'text/plain', 'text/html')
#
#
# zope.component.provideAdapter(RichtextDataConverter)
