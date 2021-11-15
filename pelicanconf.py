#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from pathlib import Path

AUTHOR = "Andrew Wray"
SITENAME = "Andrew's Website"
SITEURL = ""

PATH = "content"

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
    ("LinkedIn", "https://www.linkedin.com/in/a-wray3/"),
    ("Twitter", "https://twitter.com/AndrewWray8")
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ["images", "pdfs", "top_albums.html"]

THEME = Path("~/code/repos/pelican-blue").expanduser()
AVATAR = "/images/Prof_Pic.png"
