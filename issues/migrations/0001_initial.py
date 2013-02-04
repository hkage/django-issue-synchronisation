# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tracker'
        db.create_table(u'tracker', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('config', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(db_column='lastupdate')),
        ))
        db.send_create_signal('issues', ['Tracker'])

        # Adding model 'Issue'
        db.create_table(u'issue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=5000)),
            ('no', self.gf('django.db.models.fields.IntegerField')()),
            ('reporter', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issues.Issue'], null=True, blank=True)),
            ('tracker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issues.Tracker'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_change', self.gf('django.db.models.fields.DateTimeField')(db_column='lastchange')),
        ))
        db.send_create_signal('issues', ['Issue'])

        # Adding model 'IssueUser'
        db.create_table(u'issueuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('issue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issues.Issue'])),
        ))
        db.send_create_signal('issues', ['IssueUser'])

        # Adding model 'UserMapping'
        db.create_table(u'usermapping', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('tracker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issues.Tracker'])),
            ('login_name', self.gf('django.db.models.fields.CharField')(max_length=255, db_column='loginname')),
        ))
        db.send_create_signal('issues', ['UserMapping'])


    def backwards(self, orm):
        # Deleting model 'Tracker'
        db.delete_table(u'tracker')

        # Deleting model 'Issue'
        db.delete_table(u'issue')

        # Deleting model 'IssueUser'
        db.delete_table(u'issueuser')

        # Deleting model 'UserMapping'
        db.delete_table(u'usermapping')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'issues.issue': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Issue', 'db_table': "u'issue'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_change': ('django.db.models.fields.DateTimeField', [], {'db_column': "'lastchange'"}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issues.Issue']", 'null': 'True', 'blank': 'True'}),
            'no': ('django.db.models.fields.IntegerField', [], {}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'reporter': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tracker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issues.Tracker']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        'issues.issueuser': {
            'Meta': {'ordering': "('id',)", 'object_name': 'IssueUser', 'db_table': "u'issueuser'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issues.Issue']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'issues.tracker': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Tracker', 'db_table': "u'tracker'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'config': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'db_column': "'lastupdate'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        },
        'issues.usermapping': {
            'Meta': {'ordering': "('id',)", 'object_name': 'UserMapping', 'db_table': "u'usermapping'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "'loginname'"}),
            'tracker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issues.Tracker']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['issues']