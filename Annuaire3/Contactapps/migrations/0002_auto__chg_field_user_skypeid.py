# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'User.skypeid'
        db.alter_column('Contactapps_user', 'skypeid', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):

        # Changing field 'User.skypeid'
        db.alter_column('Contactapps_user', 'skypeid', self.gf('django.db.models.fields.IntegerField')(max_length=255))

    models = {
        'Contactapps.contact': {
            'Meta': {'object_name': 'Contact'},
            'birthday': ('django.db.models.fields.DateTimeField', [], {}),
            'date_creation': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'names': ('django.db.models.fields.TextField', [], {}),
            'secondnames': ('django.db.models.fields.TextField', [], {})
        },
        'Contactapps.lieu': {
            'Meta': {'object_name': 'Lieu'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pays': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'Contactapps.user': {
            'Meta': {'object_name': 'User'},
            'date_creation': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password_hash': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'password_salt': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True'}),
            'skypeid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['Contactapps']