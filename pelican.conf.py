#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"ram"
SITENAME = u"Ram Parthasarathy"
SITEURL = 'ramanuj.me'
TIMEZONE = 'America/New_York'

DEFAULT_LANG='en'

THEME = 'theme'

# static files to copy into root, very useful for robots.txt
FILES_TO_COPY = (
   ('extra/robots.txt', 'robots.txt'),
   ('extra/humans.txt', 'humans.txt'),
)
# directories to be copied into output/static/
STATIC_PATHS = ['img', 'css', 'js', 'fonts']

# very useful for debugging purposes
DELETE_OUTPUT_DIRECTORY = True

DEFAULT_PAGINATION = 10
DEFAULT_DATE_FORMAT = '%b %d, %Y'
