# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Project.image'
        db.alter_column(u'briansdojo_project', 'image', self.gf(u'sorl.thumbnail.fields.ImageField')(max_length=255))

    def backwards(self, orm):

        # Changing field 'Project.image'
        db.alter_column(u'briansdojo_project', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=255))

    models = {
        u'briansdojo.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'sender': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sent': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'briansdojo.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['briansdojo']