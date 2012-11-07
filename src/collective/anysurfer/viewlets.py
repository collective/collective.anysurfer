import logging
from cgi import escape

from zope.component import getMultiAdapter
from zope.annotation.interfaces import IAnnotations
from zope.i18n import translate

from Products.CMFPlone.utils import safe_unicode

from plone.app.layout.viewlets import common

from collective.anysurfer.layout import SKIN_TEMPLATE_KEY

logger = logging.getLogger('collective.anysurfer')


class TitleViewlet(common.TitleViewlet):

    def update(self):
        portal_state = getMultiAdapter((self.context, self.request),
                                        name=u'plone_portal_state')
        context_state = getMultiAdapter((self.context, self.request),
                                         name=u'plone_context_state')
        page_title = escape(safe_unicode(context_state.object_title()))
        portal_title = escape(safe_unicode(portal_state.portal_title()))
        if page_title == portal_title:
            logger.warn('View without explicit title: %s' % self.request.URL)
            self.site_title = portal_title
        else:
            self.site_title = u"%s &mdash; %s" % (page_title, portal_title)


class TitleViewletForSkinTemplateView(common.TitleViewlet):

    def update(self):
        portal_state = getMultiAdapter((self.context, self.request),
                                        name=u'plone_portal_state')
        portal_title = escape(safe_unicode(portal_state.portal_title()))
        template = IAnnotations(self.view)[SKIN_TEMPLATE_KEY]
        if template.title:
            view_title = translate(template.title, 'plone',
                    context=self.request)
            self.site_title = u"%s &mdash; %s" % (view_title, portal_title)
        else:
            logger.warn('Skin template without explicit title: %s'
                    % template.id)
            self.site_title = portal_title
