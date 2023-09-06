# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'raiders-handbook'
copyright = '2023, Streus.2135'
author = 'Streus.2135'
release = 'v1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.githubpages',
    'sphinx_favicon'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

# -- Favicon configuration -------------------------------------------------
# https://sphinx-favicon.readthedocs.io/en/latest/

favicons = [
   {
      "sizes": "16x16",
      "href": "https://secure.example.com/favicon/favicon-16x16.png",
   },
   {
      "sizes": "32x32",
      "href": "https://secure.example.com/favicon/favicon-32x32.png",
   }
]