# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table('Contactapps_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('skypeid', self.gf('django.db.models.fields.IntegerField')(max_length=255)),
            ('password_salt', self.gf('django.db.models.fields.CharField')(max_length=8, null=True)),
            ('password_hash', self.gf('django.db.models.fields.CharField')(max_length=40, null=True)),
            ('date_creation', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('Contactapps', ['User'])

        # Adding model 'Contact'
        db.create_table('Contactapps_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('names', self.gf('django.db.models.fields.TextField')()),
            ('secondnames', self.gf('django.db.models.fields.TextField')()),
            ('birthday', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_creation', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('Contactapps', ['Contact'])

        # Adding model 'Lieu'
        db.create_table('Contactapps_lieu', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pays', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ville', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('Contactapps', ['Lieu'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table('Contactapps_user')

        # Deleting model 'Contact'
        db.delete_table('Contactapps_contact')

        # Deleting model 'Lieu'
        db.delete_table('Contactapps_lieu')


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
            'skypeid': ('django.db.models.fields.IntegerField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['Contactapps']