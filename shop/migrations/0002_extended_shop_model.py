# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Category.pub_date'
        db.delete_column('shop_category', 'pub_date')

        # Adding field 'Category.active'
        db.add_column('shop_category', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Category.created'
        db.add_column('shop_category', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 11, 9, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Category.modified'
        db.add_column('shop_category', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 11, 9, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Category.pub_date'
        db.add_column('shop_category', 'pub_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 11, 9, 0, 0)),
                      keep_default=False)

        # Deleting field 'Category.active'
        db.delete_column('shop_category', 'active')

        # Deleting field 'Category.created'
        db.delete_column('shop_category', 'created')

        # Deleting field 'Category.modified'
        db.delete_column('shop_category', 'modified')


    models = {
        'shop.category': {
            'Meta': {'object_name': 'Category'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'amazon_id': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'shop.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'popularity': ('django.db.models.fields.IntegerField', [], {}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['shop']