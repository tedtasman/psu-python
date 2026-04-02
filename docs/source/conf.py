# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "psu-python"
copyright = "2026, Theodore Tasman"
author = "Theodore Tasman"
version = "0.2.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#1e407c",
        "color-brand-content": "#001e44",
        "color-background-primary": "#ffffff",
        "color-background-secondary": "#96BEE6",
        "color-foreground-primary": "#001e44",
    },
    "dark_css_variables": {
        "color-brand-primary": "#96BEE6",
        "color-brand-content": "#CCDAE6",
        "color-background-primary": "#001e44",
        "color-background-secondary": "#1e407c",
        "color-foreground-primary": "#ffffff",
    },
}

# Set the path to the source code directory
sys.path.insert(0, os.path.abspath("../../src"))

# -- Autodoc configuration --------------------------------------------------
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}
