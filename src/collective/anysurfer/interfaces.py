# -*- coding: utf-8 -*-
from collective.anysurfer import _
from collective.anysurfer.utils import get_default_text_translations
from collective.z3cform.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield.registry import DictRow
# from plone.autoform import directives as form
from plone.autoform.directives import widget
# from plone.app.z3cform.wysiwyg import WysiwygFieldWidget
from plone.supermodel import model
from plone.theme.interfaces import IDefaultPloneLayer
from zope import schema
from zope.interface import Interface


class ILayerSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""


class ISkinTemplateView(Interface):
    """Marker interface added when CMF skin template is rendered."""


# Interface
class ITextRowSchema(model.Schema):

    language = schema.TextLine(
        title=_(u"Language"),
        description=_(u'Enter the language code. Ex.: en'),
    )

#    form.widget("text", WysiwygFieldWidget)
    text = schema.Text(
        title=_(u"Text"),
    )


class IAnysurferSettings(model.Schema):
    """Schema for the control panel form."""

    accessibility_translations = schema.List(
        title=_(u"Text to show your visitor"),
        required=True,
        description=_(
            u"help_text", default=u"The text of the accessibility explanation."
        ),
        value_type=DictRow(
            title=u"Value",
            schema=ITextRowSchema,
        ),
        defaultFactory=get_default_text_translations,
    )
    widget(accessibility_translations=DataGridFieldFactory)
