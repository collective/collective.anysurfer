# -*- coding: utf-8 -*-
from collective.anysurfer import _
from collective.anysurfer import get_default_text
from collective.anysurfer import IS_PLONE4
from zope.interface import Interface
from plone.autoform import directives as form
from plone.supermodel import model
from plone.theme.interfaces import IDefaultPloneLayer
from zope import schema


class ILayerSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""


class ISkinTemplateView(Interface):
    """Marker interface added when CMF skin template is rendered."""


class IAnysurferSettings(model.Schema):
    """Schema for the control panel form."""

    if IS_PLONE4:
        # IS_PLONE4: remove on deprecation of Plone 4.3
        from plone.app.z3cform.wysiwyg import WysiwygFieldWidget

        form.widget("text", WysiwygFieldWidget)
    else:
        form.widget("text", klass="pat-tinymce")
    text = schema.Text(
        title=_(u"title_text", default=u"Body text"),
        description=_(
            u"help_text", default=u"The text of the accessibility explanation."
        ),
        required=True,
        defaultFactory=get_default_text,
    )
