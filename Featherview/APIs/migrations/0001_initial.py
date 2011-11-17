# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Api'
        db.create_table('APIs_api', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(max_length=30)),
            ('key', self.gf('django.db.models.fields.TextField')(max_length=100)),
            ('secret', self.gf('django.db.models.fields.TextField')(max_length=100)),
        ))
        db.send_create_signal('APIs', ['Api'])


    def backwards(self, orm):
        
        # Deleting model 'Api'
        db.delete_table('APIs_api')


    models = {
        'APIs.api': {
            'Meta': {'object_name': 'Api'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.TextField', [], {'max_length': '30'}),
            'secret': ('django.db.models.fields.TextField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['APIs']
