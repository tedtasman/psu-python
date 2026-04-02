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
version = "0.2.2"

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
        "color-brand-primary": "#001e44",
        "color-brand-content": "#001e44",
        "color-background-primary": "#ffffff",
        "color-background-secondary": "#A2AAAD",
        "color-foreground-primary": "#001e44",
        "color-problematic": "#009CDE",
        "color-api-name": "#009CDE",
    },
    "dark_css_variables": {
        "color-brand-primary": "#CCDAE6",
        "color-brand-content": "#CCDAE6",
        "color-background-primary": "#001e44",
        "color-background-secondary": "#000321",
        "color-foreground-primary": "#ffffff",
        "color-problematic": "#009CDE",
        "color-api-name": "#009CDE",
    },
}

# Set the path to the source code directory
sys.path.insert(0, os.path.abspath("../../src"))

# -- Autodoc configuration --------------------------------------------------
add_module_names = False

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}
