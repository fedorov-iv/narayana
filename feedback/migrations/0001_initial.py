# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MailTemplate'
        db.create_table(u'feedback_mailtemplate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('from_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('from_email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('admin_email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('copy_emails', self.gf('django.db.models.fields.EmailField')(max_length=255, blank=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('body', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'feedback', ['MailTemplate'])

        # Adding model 'FeedbackSubject'
        db.create_table(u'feedback_feedbacksubject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'feedback', ['FeedbackSubject'])

        # Adding model 'Feedback'
        db.create_table(u'feedback_feedback', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedback.FeedbackSubject'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('is_answer_needed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 4, 10, 0, 0))),
        ))
        db.send_create_signal(u'feedback', ['Feedback'])


    def backwards(self, orm):
        # Deleting model 'MailTemplate'
        db.delete_table(u'feedback_mailtemplate')

        # Deleting model 'FeedbackSubject'
        db.delete_table(u'feedback_feedbacksubject')

        # Deleting model 'Feedback'
        db.delete_table(u'feedback_feedback')


    models = {
        u'feedback.feedback': {
            'Meta': {'ordering': "['-create_date', '-id']", 'object_name': 'Feedback'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 4, 10, 0, 0)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_answer_needed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.FeedbackSubject']"}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'feedback.feedbacksubject': {
            'Meta': {'ordering': "['id']", 'object_name': 'FeedbackSubject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'feedback.mailtemplate': {
            'Meta': {'ordering': "['id']", 'object_name': 'MailTemplate'},
            'admin_email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'body': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'copy_emails': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'blank': 'True'}),
            'from_email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'from_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['feedback']