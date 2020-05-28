from plone.app.layout.globals import context
from plone.memoize.view import memoize
from Products.CMFCore.utils import getToolByName
from Products.PageTemplates.PageTemplate import PageTemplate


class ContextState(context.ContextState):
    @memoize
    def is_skin_template(self):
        template = self.get_skin_template()
        if template is None:
            return False
        else:
            return isinstance(template, PageTemplate)

    @memoize
    def get_skin_template(self):
        portal = getToolByName(self.context, "portal_url").getPortalObject()
        template_id = self.current_base_url().split("/")[-1]
        return getattr(portal, template_id, None)
