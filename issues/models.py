# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Type(models.Model):
    """Represents a type of issue tracker.

    The type is used to distinguish between different issue trackers.
    """

    class Meta:
        db_table = u'trackertype'
        ordering = ('id',)
        verbose_name = _(u'Type')
        verbose_name_plural = _(u'Types')

    cid = models.CharField(unique=True, max_length=100, verbose_name=_(u'CID'))
    name = models.CharField(max_length=60, verbose_name=_(u'Name'))
    description = models.CharField(max_length=255, blank=True, null=True,
                                   verbose_name=_(u'Description'))

    def __unicode__(self):
        return self.name


class Tracker(models.Model):
    """Reflects an issue tracker."""

    class Meta:
        db_table = u'tracker'
        ordering = ('id',)
        verbose_name = _(u'Issue tracker')
        verbose_name_plural = _(u'Issue tracker')

    type = models.ForeignKey('Type', verbose_name=_(u'Type'))
    name = models.CharField(max_length=60, verbose_name=_(u'Name'))
    config = models.CharField(max_length=255,
                              verbose_name=_(u'Configuration string'))
    active = models.BooleanField(verbose_name=_(u'Active?'))
    last_update = models.DateTimeField(verbose_name=_(u'Last update'))

    def __unicode__(self):
        return self.name


class Issue(models.Model):
    """Basic issue storage class used for all issue trackers."""

    class Meta:
        db_table = u'issue'
        ordering = ('id',)
        verbose_name = _(u'Issue')
        verbose_name_plural = _(u'Issues')

    title = models.CharField(max_length=255, verbose_name=_(u'Title'))
    description = models.CharField(db_column='ti_beschreibung',
                                   max_length=5000,
                                   verbose_name=_(u'Description'))
    # The internal issue number (depends on the issue tracker)
    no = models.IntegerField(verbose_name=_(u'No.'))
    reporter = models.CharField(max_length=250, verbose_name=_(u'Reporter'))
    owner = models.CharField(max_length=250,
                             verbose_name=_(u'Owner'))
    active = models.BooleanField(verbose_name=_(u'Active?'))
    master = models.ForeignKey('Issue', blank=True, null=True)
    tracker = models.ForeignKey('Tracker', verbose_name=_(u'Issue tracker'))
    # Local timestamps
    created = models.DateTimeField(verbose_name=_(u'Creation date'))
    updated = models.DateTimeField(verbose_name=_(u'Update date'))
    # Remote timestamps
    last_change = models.DateTimeField(verbose_name=_(u'Last change'))

    def __unicode__(self):
        return self.get_title() or str(self.__class__)

    @classmethod
    def by_tracker_id(cls, tracker, issue_no):
        """Returns an issue by its tracker.

        :param tracker: A :class:`Tracker` instance or id
        :param issue_no: The issue number (from within the tracker)
        :returns: Instance of :class:`Issue`
        """
        query = Issue.objects.filter(tracker=tracker, no=issue_no)
        if query.count() == 0:
            return Issue()
        else:
            return query[0]

    def get_title(self):
        """Returns the title of an issue.

        :returns: Title of the issue as a string.
        """
        if self.no and self.title:
            master = u''
            if self.master:
                master = u' (#%s)' % self.master.no
            return u'#%d%s: %s' % (self.no, master, self.title)
        elif not self.no and self.title:
            return self.title
        else:
            return None

    def set_title(self, value):
        """Set the title and strip value if necessary.

        :param value: The title value
        """
        assert isinstance(value, basestring)
        self.title = value[:255]

    def set_description(self, value):
        """Set the description and strip value if necessary.

        :param value: The title value
        """
        assert isinstance(value, basestring)
        self.description = value[:5000]


class IssueUser(models.Model):
    """Which users are related to an issue?."""

    user = models.ForeignKey(User, verbose_name=_(u'User'))
    issue = models.ForeignKey('Issue', verbose_name=_(u'Issue'))

    class Meta:
        db_table = u'issueuser'
        ordering = ('id',)
        verbose_name = _(u'Issue user')
        verbose_name_plural = _(u'Issue users')


class UserMapping(models.Model):
    """Defines a mapping between a user's issue tracking name and the internal user."""

    user = models.ForeignKey(User, verbose_name=_(u'User'))
    tracker = models.ForeignKey('Tracker', verbose_name=_(u'Issue tracker'))
    login_name = models.CharField(max_length=255,
                                  verbose_name=_(u'Login name'))

    class Meta:
        db_table = u'usermapping'
        ordering = ('id',)
        verbose_name = _(u'User mapping')
        verbose_name_plural = _(u'User mapping')
