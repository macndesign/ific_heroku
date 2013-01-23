# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SalaImprensa'
        db.create_table('website_salaimprensa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, blank=True)),
            ('data_pub', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 23, 0, 0))),
            ('subtitulo', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('video', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('texto', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('destaque', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('website', ['SalaImprensa'])

        # Adding model 'Equipe'
        db.create_table('website_equipe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ordem', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('resumo', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('site', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('data_pub', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 23, 0, 0))),
        ))
        db.send_create_signal('website', ['Equipe'])

        # Adding model 'Galeria'
        db.create_table('website_galeria', (
            ('ordem', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('texto', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('data_pub', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 23, 0, 0))),
        ))
        db.send_create_signal('website', ['Galeria'])

        # Adding model 'PublicacaoCientifica'
        db.create_table('website_publicacao_cientifica', (
            ('ordem', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('descricao', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('arquivo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('website', ['PublicacaoCientifica'])


    def backwards(self, orm):
        # Deleting model 'SalaImprensa'
        db.delete_table('website_salaimprensa')

        # Deleting model 'Equipe'
        db.delete_table('website_equipe')

        # Deleting model 'Galeria'
        db.delete_table('website_galeria')

        # Deleting model 'PublicacaoCientifica'
        db.delete_table('website_publicacao_cientifica')


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
            'texto': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'subtitulo': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'video': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['website']