#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Andrew Wray"
SITENAME = "Andrew's Blog"
SITEURL = ""
# SITELOGO = SITEURL + "/images/profile.png"
# MAIN_MENU = True


TIMEZONE = "America/Los_Angeles"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (
# ("Pelican", "https://getpelican.com/"),
# ("Python.org", "https://www.python.org/"),
# ("Jinja2", "https://palletsprojects.com/p/jinja/"),
# ("You can modify those links in your config file", "#"),
# )

# Social widget
SOCIAL = (
    ("Github", "https://github.com/awray3"),
    ("LinkedIn", "https://www.linkedin.com/in/andrew-wray3/"),
    ("Twitter", "https://twitter.com/AndrewWray8"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# PATH-RELATED
PATH = "content"
OUTPUT_PATH = "docs"
ARTICLE_PATHS = ["blog"]
STATIC_PATHS = ["images", "pdfs", "gifs", "extra"]
ARTICLE_EXCLUDES = ["extras/top_albums.html"]
EXTRA_PATH_METADATA = {
    "extra/top_albums.html": {"path": "top_albums.html"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}
# PLUGIN_PATHS = ["./plugins"]
PLUGINS = ["render_math"]

THEME = "themes/simple-bootstrap"
AVATAR = "images/Prof_Pic.png"
