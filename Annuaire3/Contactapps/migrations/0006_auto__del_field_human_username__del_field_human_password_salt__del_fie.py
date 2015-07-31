# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Human.username'
        db.delete_column('Contactapps_human', 'username')

        # Deleting field 'Human.password_salt'
        db.delete_column('Contactapps_human', 'password_salt')

        # Deleting field 'Human.date_creation'
        db.delete_column('Contactapps_human', 'date_creation')

        # Deleting field 'Human.password_hash'
        db.delete_column('Contactapps_human', 'password_hash')

        # Adding field 'Human.user'
        db.add_column('Contactapps_human', 'user',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['auth.User'], unique=True),
                      keep_default=False)

        # Adding field 'Human.signature'
        db.add_column('Contactapps_human', 'signature',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Human.online'
        db.add_column('Contactapps_human', 'online',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2015, 7, 31, 0, 0), max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Human.username'
        db.add_column('Contactapps_human', 'username',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=255),
                      keep_default=False)

        # Adding field 'Human.password_salt'
        db.add_column('Contactapps_human', 'password_salt',
                      self.gf('django.db.models.fields.CharField')(max_length=8, null=True),
                      keep_default=False)

        # Adding field 'Human.date_creation'
        db.add_column('Contactapps_human', 'date_creation',
                      self.gf('django.db.models.fields.DateTimeField')(default=''),
                      keep_default=False)

        # Adding field 'Human.password_hash'
        db.add_column('Contactapps_human', 'password_hash',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True),
                      keep_default=False)

        # Deleting field 'Human.user'
        db.delete_column('Contactapps_human', 'user_id')

        # Deleting field 'Human.signature'
        db.delete_column('Contactapps_human', 'signature')

        # Deleting field 'Human.online'
        db.delete_column('Contactapps_human', 'online')


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'online': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'signature': ('django.db.models.fields.TextField', [], {}),
            'skypeid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'Contactapps.lieu': {
            'Meta': {'object_name': 'Lieu'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pays': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
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
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['Contactapps']