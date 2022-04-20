# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import pathlib
import sphinx_material


# -- Project information -----------------------------------------------------

project = 'python_ml_project_skeleton'
copyright = '2022, samy khelifi and IGN/SIMV'
author = 'samy khelifi@IGN/SIMV'
this_dir = pathlib.Path(__file__).resolve().parent
with (this_dir / ".." / ".." / "VERSION").open() as vf:
    version = vf.read().strip()
print("Version as read from version.txt: '{}'".format(version))
# The full version, including alpha/beta/rc tags
release = version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
                'sphinx.ext.napoleon',
                'sphinx.ext.autosummary',
                'sphinx.ext.autodoc',
                'sphinx_material',
                'sphinx_tabs.tabs',
                "myst_parser"
              ]


# -- HTML theme settings -----------------------------------------------
html_show_sourcelink = True
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html", "version.html"]
}

html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()
html_theme = 'sphinx_material'
# Material theme options (see theme.conf for more information)

html_theme_options = {

    # Set the name of the project to appear in the navigation.
    'nav_title': 'python ml project skeleton',
    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    'base_url': 'https://samysung.github.io/python_ml_project_skeleton',
    # Set the color and the accent color
    'color_primary': 'deep-purple',
    'color_accent': 'cyan',
    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/samysung/python_ml_project_skeleton',
    'repo_name': 'python_ml_project_skeleton',
    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 3,
    # If False, expand all TOC entries
    'globaltoc_collapse': True,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False,
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


