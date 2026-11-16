from collective.anysurfer import _
from collective.anysurfer.utils import get_default_text_translations
from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield.registry import DictRow
from plone.app.textfield import RichText
from plone.autoform.directives import widget
from plone.theme.interfaces import IDefaultPloneLayer
from zope import schema
from zope.interface import Interface


class ILayerSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""


class ISkinTemplateView(Interface):
    """Marker interface added when CMF skin template is rendered."""


class ITextRowSchema(Interface):

    language = schema.TextLine(
        title=_("Language (en, fr,...)"),
        description=_("Enter the language code. Ex.: en"),
    )

    text = RichText(
        title=_("Text"),
    )


class IAnysurferSettings(Interface):
    """Schema for the control panel form."""

    accessibility_translations = schema.List(
        title=_("Multilingual accessibility statements texts"),
        description=_(
            "This text will be available through the accessibility site action"
        ),
        value_type=DictRow(
            title="Value",
            schema=ITextRowSchema,
        ),
        defaultFactory=get_default_text_translations,
        required=True,
    )
    widget(accessibility_translations=DataGridFieldFactory)
