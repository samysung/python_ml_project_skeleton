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
import os
import sys
import pathlib
import sphinx_material
import sphinx_rtd_theme
sys.path.insert(0, os.path.abspath('../'))

# -- Project information -----------------------------------------------------

project = 'python_ml_project_skeleton'
copyright = '2022, samy khelifi and IGN/SIMV'
author = 'samy khelifi@IGN/SIMV'
this_dir = pathlib.Path(__file__).resolve().parent
with (this_dir / ".." / "VERSION").open() as vf:
    version = vf.read().strip()
print("Version as read from version.txt: '{}'".format(version))
# The full version, including alpha/beta/rc tags
release = version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
theme_plugin = 'sphinx_material'
extensions = [
                'sphinx.ext.napoleon',
                'sphinx.ext.autosummary',
                'sphinx.ext.autodoc',
                theme_plugin,
                'sphinx_tabs.tabs',
                "sphinx_multiversion",
                "myst_parser"
              ]
tag_version = True
html_theme = theme_plugin
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
# -- HTML theme settings -----------------------------------------------
html_show_sourcelink = True
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html"]
}

html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()

# Material theme options (see theme.conf for more information)

html_theme_options = {

    # Set the name of the project to appear in the navigation.
    'nav_title': 'python ml project skeleton',
    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    'base_url': 'https://samysung.github.io/python_ml_project_skeleton',
    # Set the color and the accent color
    'color_primary': 'deep-purple',
    # 'color_accent': 'cyan',
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

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Sphinx multiversion configuration

# Whitelist pattern for tags (set to None to ignore all tags)
smv_tag_whitelist = r'^t\d+\.\d+$' # include tags like vX.Y (v1.2, v2.6)

# Whitelist pattern for branches (set to None to ignore all branches)
smv_branch_whitelist = r'^.*$'

# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = None

# Pattern for released versions
smv_released_pattern = r'^tags/.*$'

# Format for versioned output directories inside the build directory
smv_outputdir_format = '{ref.name}'

# Determines whether remote or local git branches/tags are preferred if their output dirs conflict
smv_prefer_remote_refs = False


