from setuptools import setup

version = "2.0.0.dev0"

long_description = (
    open("README.md").read()
    + "\n"
    + open("CONTRIBUTORS.md").read()
    + "\n"
    + open("CHANGES.md").read()
    + "\n"
)

setup(
    name="collective.anysurfer",
    version=version,
    description="Anysurfer (Belgian accessibility standard) support for Plone",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: 6.2",
        "Framework :: Plone :: Addon",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="",
    author="",
    author_email="",
    url="https://github.com/collective/collective.anysurfer/",
    license="gpl",
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "z3c.jbot",
        "plone.api",
        "beautifulsoup4",
        "collective.z3cform.datagridfield",
        # -*- Extra requirements: -*-
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            "unittest2",
        ]
    },
    entry_points="""
      # -*- Entry points: -*-
  	  [z3c.autoinclude.plugin]
  	  target = plone
      """,
)
