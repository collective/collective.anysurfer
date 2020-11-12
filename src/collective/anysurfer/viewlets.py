import logging
import six

from cgi import escape
from collective.anysurfer.layout import SKIN_TEMPLATE_KEY
from plone import api
from plone.app.layout.viewlets import common
from Products.CMFPlone.utils import safe_unicode
from zExceptions import NotFound
from zope.annotation.interfaces import IAnnotations
from zope.component import getMultiAdapter
from zope.i18n import translate

logger = logging.getLogger("collective.anysurfer")


class TitleViewlet(common.TitleViewlet):
    def update(self):
        portal_state = getMultiAdapter(
            (self.context, self.request), name=u"plone_portal_state"
        )
        context_state = getMultiAdapter(
            (self.context, self.request), name=u"plone_context_state"
        )
        page_title = escape(safe_unicode(context_state.object_title()))
        root_title = escape(safe_unicode(portal_state.navigation_root_title()))
        if page_title == root_title:
            logger.warn("View without explicit title: %s" % self.request.URL)
            view_name = self.view.__name__
            view_title = translate(view_name, "plone", context=self.request)
            if view_name == "search":
                results_nb = self.view.results().sequence_length
                view_title = translate(u"Search results", "plone", context=self.request)
                self.site_title = u"%s %s &mdash; %s" % (
                    results_nb,
                    view_title,
                    root_title,
                )
            elif view_name is not None and view_name != view_title:
                self.site_title = u"%s &mdash; %s" % (view_title, root_title)
            else:
                self.site_title = root_title
                try:
                    portal = api.portal.get()
                    url = self.request.getURL()
                    if six.PY2:
                        url = url.encode("utf8")
                    url = url.replace(portal.absolute_url(), "").lstrip("/")
                    portal.unrestrictedTraverse(url)

                except (NotFound, KeyError):
                    self.site_title = u"%s &mdash; %s" % (
                        translate(u"404-error", "plone", context=self.request),
                        root_title,
                    )
                except AttributeError:
                    pass

        else:
            self.site_title = u"%s &mdash; %s" % (page_title, root_title)


class TitleViewletForSkinTemplateView(common.TitleViewlet):
    def update(self):
        portal_state = getMultiAdapter(
            (self.context, self.request), name=u"plone_portal_state"
        )
        root_title = escape(safe_unicode(portal_state.navigation_root_title()))
        template = IAnnotations(self.view)[SKIN_TEMPLATE_KEY]
        title = template.title or template.id
        if title:
            view_title = translate(title, "plone", context=self.request)
            self.site_title = u"%s &mdash; %s" % (view_title, root_title)
        else:
            logger.warn("Skin template without explicit title: %s" % template.id)
            self.site_title = root_title
