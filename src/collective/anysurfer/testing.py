from Products.CMFCore.utils import getToolByName
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class CollectiveAnysurfer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import collective.anysurfer
        xmlconfig.file('configure.zcml',
                       collective.anysurfer,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        language_tool = getToolByName(portal, 'portal_languages')
        language_tool.addSupportedLanguage('fr')
        language_tool.setDefaultLanguage('fr')
        language_tool.use_request_negotiation = True
        language_tool.setLanguageBindings()
        applyProfile(portal, 'collective.anysurfer:default')

COLLECTIVE_ANYSURFER_FIXTURE = CollectiveAnysurfer()
COLLECTIVE_ANYSURFER_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(COLLECTIVE_ANYSURFER_FIXTURE, ),
                       name="CollectiveAnysurfer:Integration")