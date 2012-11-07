from zope.interface import alsoProvides
from zope.component import getMultiAdapter
from zope.annotation.interfaces import IAnnotations
from zope.annotation.interfaces import IAttributeAnnotatable

from plone.app.layout.globals import layout

from collective.anysurfer.interfaces import ISkinTemplateView

SKIN_TEMPLATE_KEY = 'skin_template'


class LayoutPolicy(layout.LayoutPolicy):

    def mark_view(self, view):
        super(LayoutPolicy, self).mark_view(view)

        context_state = getMultiAdapter(
            (self.context, self.request), name=u'plone_context_state')

        if (context_state.is_skin_template()
                and not ISkinTemplateView.providedBy(view)):
            alsoProvides(view, ISkinTemplateView)
            alsoProvides(view, IAttributeAnnotatable)
            template = context_state.get_skin_template()
            IAnnotations(view)[SKIN_TEMPLATE_KEY] = template
