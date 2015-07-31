# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'User'
        db.delete_table('Contactapps_user')

        # Adding model 'Human'
        db.create_table('Contactapps_human', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('skypeid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('password_salt', self.gf('django.db.models.fields.CharField')(max_length=8, null=True)),
            ('password_hash', self.gf('django.db.models.fields.CharField')(max_length=40, null=True)),
            ('date_creation', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('Contactapps', ['Human'])

        # Deleting field 'Contact.user'
        db.delete_column('Contactapps_contact', 'user_id')

        # Adding field 'Contact.human'
        db.add_column('Contactapps_contact', 'human',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['Contactapps.Human']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'User'
        db.create_table('Contactapps_user', (
            ('username', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('password_salt', self.gf('django.db.models.fields.CharField')(max_length=8, null=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_creation', self.gf('django.db.models.fields.DateTimeField')()),
            ('skypeid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('password_hash', self.gf('django.db.models.fields.CharField')(max_length=40, null=True)),
        ))
        db.send_create_signal('Contactapps', ['User'])

        # Deleting model 'Human'
        db.delete_table('Contactapps_human')

        # Adding field 'Contact.user'
        db.add_column('Contactapps_contact', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['Contactapps.User']),
                      keep_default=False)

        # Deleting field 'Contact.human'
        db.delete_column('Contactapps_contact', 'human_id')


    models = {
        'Contactapps.contact': {
            'Meta': {'object_name': 'Contact'},
            'birthday': ('django.db.models.fields.TextField', [], {}),
            'date_creation': ('django.db.models.fields.DateTimeField', [], {}),
            'human': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Contactapps.Human']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lieu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Contactapps.Lieu']"}),
            'names': ('django.db.models.fields.TextField', [], {}),
            'secondnames': ('django.db.models.fields.TextField', [], {})
        },
        'Contactapps.human': {
            'Meta': {'object_name': 'Human'},
            'date_creation': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password_hash': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'password_salt': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True'}),
            'skypeid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'Contactapps.lieu': {
            'Meta': {'object_name': 'Lieu'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pays': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['Contactapps']