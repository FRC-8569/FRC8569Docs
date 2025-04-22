# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FRC8569'
copyright = '2025, Justmore5mins FRC8569'
author = 'Justmore5mins'
release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_tabs.tabs',"sphinx_design",'sphinx.ext.autosectionlabel']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_permalinks_icon = '<span>#</span>'
html_theme = 'sphinxawesome_theme'
pygments_style = 'xcode'

html_static_path = ['_static']