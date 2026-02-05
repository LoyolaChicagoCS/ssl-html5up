from datetime import datetime

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Software and Systems Laboratory'
copyright = f"{datetime.now().year}, {project}"
author = project

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "ablog",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_design"
]

# Sphinx auto section label settings
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 2

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

# Sphinx Book Theme Settings
html_theme_options = {
    "repository_url": "https://github.com/LoyolaChicagoCS/ssl-html5up",
    "use_repository_button": True,
    "show_navbar_depth": 1,
    "collapse_navbar": True,
    "use_sidenotes": True,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/SoftwareSystemsLaboratory",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Google Scholar",
            "url": "https://scholar.google.com/citations?user=Ls7yS0IAAAAJ",
            "icon": "fa-brands fa-google-scholar",
        },
    ],
}
html_title = project
html_logo = "_static/images/headshot.png"
html_favicon = "_static/favicon.png"
