# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'rescale'
copyright = '2024, Kyle Niemeyer'
author = 'Kyle Niemeyer'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx.ext.mathjax',
]

autodoc_default_options = {'members': True}
autoclass_content = 'class'
napoleon_numpy_docstring = True
napoleon_google_docstring = False


templates_path = ['_templates']
exclude_patterns = []

intersphinx_mapping = {
  'python': ('https://docs.python.org/3.12', None),
  'numpy': ('https://docs.scipy.org/doc/numpy/', None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
