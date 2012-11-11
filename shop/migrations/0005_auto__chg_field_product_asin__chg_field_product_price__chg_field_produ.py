# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Product.asin'
        db.alter_column('shop_product', 'asin', self.gf('django.db.models.fields.CharField')(default=0, max_length=10))

        # Changing field 'Product.price'
        db.alter_column('shop_product', 'price', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'Product.popularity'
        db.alter_column('shop_product', 'popularity', self.gf('django.db.models.fields.IntegerField')(default=0))

    def backwards(self, orm):

        # Changing field 'Product.asin'
        db.alter_column('shop_product', 'asin', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

        # Changing field 'Product.price'
        db.alter_column('shop_product', 'price', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Product.popularity'
        db.alter_column('shop_product', 'popularity', self.gf('django.db.models.fields.IntegerField')(null=True))

    models = {
        'shop.additionalpage': {
            'Meta': {'object_name': 'AdditionalPage'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'shop.category': {
            'Meta': {'object_name': 'Category'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'amazon_node_id': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 11, 11, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'shop.product': {
            'Meta': {'object_name': 'Product'},
            'asin': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products'", 'to': "orm['shop.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'popularity': ('django.db.models.fields.IntegerField', [], {}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['shop']