from zope.interface import Interface

from plone.theme.interfaces import IDefaultPloneLayer


class ILayerSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""


class ISkinTemplateView(Interface):
    """Marker interface added when CMF skin template is rendered."""
