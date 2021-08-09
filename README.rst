====================
collective.anysurfer
====================

.. image:: https://api.travis-ci.com/collective/collective.anysurfer.svg?branch=master
    :target: https://travis-ci.com/github/collective/collective.anysurfer

This package adds Anysurfer (https://anysurfer.be/fr) support to Plone.
Anysurfer is a Belgian accessibility standard equivalent to WCAG 2.0 A.

This package is totally transparent for the user.
It fixes various accessibility issues in Plone, in standard features,
content types, body texts, forms, search results, ...

It also overrides Plone Accessibility info to allow its edition through
the Anysurfer control panel.


Features
--------

1. Adds missing page titles for views / skins / 404 error page
2. Add search results count in H1 and move H1 to the top
3. Add search results count in page title
4. Fixes News item image alt
5. Removes empty <ul> lists
6. Allows empty image alt
7. Fixes 'Required' labels html position
8. Replace Plone replacetag="h2" by real tag
9. Replace default Accessibility info with a multilingual editable text
10. Replace "nav" by "div" for breadcrumb (Only for Plone5. It's already a div in Plone4.)

Limitations
-----------

This add-on has been developed on Plone 4.3 (Python 2) and Plone 5.2/6 (Python 3).


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


Versions
--------

If you use Plone 4, be careful that you must pin those egg versions::

    collective.z3cform.datagridfield = 1.2
    soupsieve = 1.9.6


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.anysurfer/issues
- Source Code: https://github.com/collective/collective.anysurfer


License
-------

The project is licensed under the GPLv2.
