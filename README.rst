====================
collective.anysurfer
====================

.. image:: https://api.travis-ci.com/collective/collective.anysurfer.svg?branch=master
    :target: https://travis-ci.com/github/collective/collective.anysurfer

This package adds Anysurfer (https://anysurfer.be/fr) support to Plone.
Anysurfer is a Belgian accessibility standard equivalent to WCAG 2.0 A.

This package is totally transparent for the user.
It fixes various accessibility issues in Plone, in standard features,
content types, body texts, ...

It also overrides Plone Accessibility info skin to allow its edition through
the Anysurfer control panel.


Features
--------

1. Adds missing page titles for views / skins / 404 error page
2. Improves search results count (in H1 and page title)
3. Fixes News item image alt
4. Removes empty <ul> lists
5. Allows empty image alt
6. Fixes 'Required' labels html position
7. Replace Plone replacetag="h2" by real tag
8. Replace default Accessibility info with a multilingual editable text


Limitations
-----------

This add-on has been developed on Plone 4.3.
It is not yet fully compatible with Plone 5.


Translations
------------

This product has been translated into

- English
- French
- Dutch (with missing translations)


Installation
------------

Install collective.anysurfer by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.anysurfer


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.anysurfer/issues
- Source Code: https://github.com/collective/collective.anysurfer


License
-------

The project is licensed under the GPLv2.
