# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'SalaImprensa.slug'
        db.alter_column('website_salaimprensa', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=120, null=True))

    def backwards(self, orm):

        # Changing field 'SalaImprensa.slug'
        db.alter_column('website_salaimprensa', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True))

    models = {
        'website.equipe': {
            'Meta': {'ordering': "['ordem']", 'object_name': 'Equipe'},
            'data_pub': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 23, 0, 0)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'ordem': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'resumo': ('django.db.models.fields.TextField', [], {}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'website.galeria': {
            'Meta': {'ordering': "['ordem']", 'object_name': 'Galeria'},
            'data_pub': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 23, 0, 0)'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ordem': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'thumb': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'website.publicacaocientifica': {
            'Meta': {'ordering': "['ordem', 'titulo']", 'object_name': 'PublicacaoCientifica', 'db_table': "'website_publicacao_cientifica'"},
            'arquivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'descricao': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ordem': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'})
        },
        'website.salaimprensa': {
            'Meta': {'ordering': "['-data_pub']", 'object_name': 'SalaImprensa'},
            'data_pub': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 23, 0, 0)'}),
            'destaque': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'subtitulo': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'video': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['website']