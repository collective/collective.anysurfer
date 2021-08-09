Changelog
=========

1.4.4 (2021-08-09)
------------------

- Add Plone 6 compatibility.
  [bsuttor]


1.4.3 (2021-07-31)
------------------

- Fix import from collective.z3cform.datagridfield
  [laulaz]

- Fix python3 compatibility : use html.escape instead of cgi.escape
  [boulch]


1.4.2 (2021-01-06)
------------------

- Breadcrumb is already in a "div" in Plone4, so, we override plone.app.layout.viewlets.path_bar.pt. only for Plone5.
  [boulch]


1.4.1 (2021-01-04)
------------------

- Override plone.app.layout.viewlets.path_bar.pt. Change <nav> to <div>
  [boulch]


1.4 (2020-11-18)
----------------

- Add Plone 5 (Python 3) compatibility
  [boulch, laulaz]

- Add uninstall profile
  [laulaz]


1.3.4 (2020-11-04)
------------------

- Content types images should be inside links in search results
  [laulaz]


1.3.3 (2020-06-17)
------------------

- Avoid displaying 'None' title for unknown browser views
  [laulaz]

- Avoid traversal error with unicode urls
  [laulaz]


1.3.2 (2020-06-15)
------------------

- Fix multilingual default text translations at install : #3
  [laulaz]


1.3.1 (2020-05-28)
------------------

- Fix upgrade steps (1.2 -> 1.3)
  [laulaz]


1.3 (2020-05-28)
----------------

- Override Accessibility info with a multilingual / editable / filled by default
  text. The text can be changed in a new Anysurfer control panel (upgrade step
  included)
  [boulch, laulaz]

- Fix 404 / EN pages title handling
  [laulaz]

- Update/fix buildout & tests
  [boulch, laulaz]

- Make titles calculation more robust in [uni/multi]lingual websites : #1
  [laulaz]


1.2.2 (2020-04-29)
------------------

- Fix view titles calculation in multilingual websites : #1
  [laulaz]

- Add missing plone.api dependency
  [laulaz]


1.2.1 (2019-11-20)
------------------

- Harmonization of '(Required)' syntax for fields
  [laulaz]


1.2 (2019-10-04)
----------------

- Add documentation, contributors, fix setup.py & use RST
  [laulaz]

- Handle more Anysurfer usecases : empty lists, bad alts, required labels, ...
  [laulaz]

- Move h1, add search results count in search page title & handle JS refresh
  [laulaz]

- Handle 404 page
  [vpiret]

- Migrate to plone 5
  [oxydedefer]

- Add missing translations for accessibility view title
  [laulaz]

- Add missing translations for contact-info view title
  [laulaz]


1.1 (2012-11-12)
----------------

- Nothing changed yet.


1.0 (2012-11-09)
----------------

- Package created using zopeskel
  []
