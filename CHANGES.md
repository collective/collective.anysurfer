# Changelog

<!-- towncrier release notes start -->

## 2.0.0 (unreleased)


- Breaking: replace the `pkg_resources` namespace of `collective` with a
  PEP 420 native namespace. Support Plone 6.1 only on Python 3.10 to 3.13,
  and Plone 6.2 on Python 3.10 to 3.14. Use 1.4.x for Plone 4.3 to 6.0.
  [remdub]

- Drop the Python 2 and Plone 4 code: `HAS_PLONE_5` and `HAS_PLONE_6` (which
  called `plone.api` at import time), the Plone 4 language handling and
  `search.js`, and the overrides of templates that no longer exist
  (accessibility-info skin template, `plone.app.search`). Register
  `search.js` and the breadcrumb viewlet without `zcml:condition`.
  [remdub]

- Import `INonInstallable`, `IPloneSiteRoot` and `safe_text` from
  `plone.base` instead of the aliases Plone 6.2 deprecates. Port the tests to
  `unittest`, `plone.testing.zope` and `get_installer`: they could no longer
  run on Python 3.10+ (`unittest2`) nor on Plone 5.2+ (`portal_quickinstaller`).
  [remdub]

- Configure the package with plone.meta 2.12.0 (test matrix on Plone 6.2.3
  and 6.1), move its metadata to `pyproject.toml`, convert the documentation
  to Markdown and run the development environment on Plone 6.2.3 with uv
  instead of buildout. Drop Travis and the buildout configuration.
  [remdub]


## 1.4.7 (2022-10-18)

- Change permissions : By default, configlet should be accessible for Manager AND Site Administrator
  [boulch]


## 1.4.6 (2022-08-17)

- Fix import error for `ILanguageSchema` on Plone 5.2 / 6
  [laulaz]


## 1.4.5 (2022-01-19)

- Get rid of includeDependencies for Plone 6 compatibility
  [laulaz]

- Add `from_encoding` parameter to BeautifulSoup transformations to fix encoding.
  [boulch]

- Include CMFCore permissions to avoid potential ComponentLookupError
  [laulaz]


## 1.4.4 (2021-08-09)

- Add Plone 6 compatibility.
  [bsuttor]


## 1.4.3 (2021-07-31)

- Fix import from collective.z3cform.datagridfield
  [laulaz]

- Fix python3 compatibility : use html.escape instead of cgi.escape
  [boulch]


## 1.4.2 (2021-01-06)

- Breadcrumb is already in a "div" in Plone4, so, we override plone.app.layout.viewlets.path_bar.pt. only for Plone5.
  [boulch]


## 1.4.1 (2021-01-04)

- Override plone.app.layout.viewlets.path_bar.pt. Change `<nav>` to `<div>`
  [boulch]


## 1.4 (2020-11-18)

- Add Plone 5 (Python 3) compatibility
  [boulch, laulaz]

- Add uninstall profile
  [laulaz]


## 1.3.4 (2020-11-04)

- Content types images should be inside links in search results
  [laulaz]


## 1.3.3 (2020-06-17)

- Avoid displaying 'None' title for unknown browser views
  [laulaz]

- Avoid traversal error with unicode urls
  [laulaz]


## 1.3.2 (2020-06-15)

- Fix multilingual default text translations at install : #3
  [laulaz]


## 1.3.1 (2020-05-28)

- Fix upgrade steps (1.2 -> 1.3)
  [laulaz]


## 1.3 (2020-05-28)

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


## 1.2.2 (2020-04-29)

- Fix view titles calculation in multilingual websites : #1
  [laulaz]

- Add missing plone.api dependency
  [laulaz]


## 1.2.1 (2019-11-20)

- Harmonization of '(Required)' syntax for fields
  [laulaz]


## 1.2 (2019-10-04)

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


## 1.1 (2012-11-12)

- Nothing changed yet.


## 1.0 (2012-11-09)

- Package created using zopeskel
  []
