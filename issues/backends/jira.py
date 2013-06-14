# -*- coding: utf-8 -*-

"""Jira interface"""

from issues.core import TrackerPlugin


class JiraRPC(TrackerPlugin):

    id = 4
    name = 'JIRA issue synchronization'

    def sync(self, tracker):
        return True
