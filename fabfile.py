"""Fabric tasks for publishing a pelican blog to github."""
from __future__ import with_statement

from fabric.api import lcd, local, settings


def pelican():
    """Re-generates the output."""
    local('pelican -s pelican.conf.py .')


def push(commit_message):
    """Commits the current changes."""
    local('git add .')
    with settings(warn_only=True):
        local('git commit -am "{0}"'.format(commit_message))
    local('git push origin')


def publish(commit_message):
    """Re-generates the blog, commits and pushes to github."""
    push(commit_message)
    pelican()
    local('cp -R output/ ~/pandora/ramanujam.github.com/')
    with lcd('~/pandora/ramanujam.github.com/'):
        local('git add .')
        with settings(warn_only=True):
            local('git commit -am "pelican autocommit"')
        local('git push origin master')
