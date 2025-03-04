# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GSEApy-fGSEA comparison'
copyright = '2025, Shakira Agata'
author = 'Shakira Agata'
release = '2025'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['nbsphinx',
              'sphinx_rtd_theme'
             ]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

html_js_files = [
    'custom.js',
]

html_css_files = [
    'custom.css',
]

