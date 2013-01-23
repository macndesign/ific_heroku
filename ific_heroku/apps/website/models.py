# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
import datetime

# Create your models here.
class SalaImprensa(models.Model):
    titulo = models.CharField(u'Título', max_length=120)
    slug = models.SlugField(unique_for_date=True, null=True, blank=True)
    data_pub = models.DateTimeField(u'Data de publicação', default=datetime.datetime.now())
    subtitulo = models.CharField(u'Subtítulo', max_length=120, null=True, blank=True)
    video = models.TextField(u'Vídeo', null=True, blank=True)
    texto = models.TextField('Texto', null=True, blank=True)
    link = models.CharField(u'Link', max_length=120, null=True, blank=True)
    foto = models.ImageField('Foto', upload_to='images/sala_imprensa', null=True, blank=True)
    destaque = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
            super(SalaImprensa, self).save(*args, **kwargs)
    
    class Meta:
        db_table = 'website_salaimprensa'
        verbose_name = u'Sala de imprensa'
        verbose_name_plural = u'Salas de imprensa'
        ordering = ['-data_pub']

    def get_absolute_url(self):
        return reverse(
            'core:noticia',
            args=[
                str(self.data_pub.year),
                str(self.data_pub.month).zfill(2),
                str(self.data_pub.day).zfill(2),
                str(self.slug),
            ]
        )


    def __unicode__(self):
        return self.titulo


class Equipe(models.Model):
    ordem = models.PositiveSmallIntegerField(default=0)
    nome = models.CharField('Nome', max_length=120)
    resumo = models.TextField(u'Resumo do currículo')
    email = models.EmailField('Email', null=True, blank=True)
    site = models.URLField('Site', verify_exists=False, null=True, blank=True)
    foto = models.ImageField('Foto do colaborador', upload_to='images/equipe', null=True, blank=True)
    data_pub = models.DateTimeField(u'Data de publicação', default=datetime.datetime.now())
    
    class Meta:
        db_table = 'website_equipe'
        verbose_name = u'Membro da equipe'
        verbose_name_plural = u'Membros da equipe'
        ordering = ['ordem']
    
    def __unicode__(self):
        return self.nome


class Galeria(models.Model):
    ordem = models.AutoField(u'Ordenação das fotos', primary_key=True)
    foto = models.ImageField('Foto', upload_to='images/gallery', null=True, blank=True)
    texto = models.TextField(u'Subtítulo da foto', null=True, blank=True)
    data_pub = models.DateTimeField(u'Data de publicação', default=datetime.datetime.now())

    class Meta:
        db_table = 'website_galeria'
        verbose_name = u'Galeria'
        verbose_name_plural = u'Galerias'
        ordering = ['ordem']

    def __unicode__(self):
        return '%d - %s' % (self.ordem, self.texto)

class PublicacaoCientifica(models.Model):
    ordem = models.AutoField(u'Ordenação das fotos', primary_key=True)
    titulo = models.CharField(u'Título', max_length=120, null=True, blank=True)
    descricao = models.TextField(u'Descrição', null=True, blank=True)
    arquivo = models.FileField(upload_to='docs/publicacoes')

    class Meta:
        db_table = 'website_publicacao_cientifica'
        verbose_name = u'Publicação científica'
        verbose_name_plural = u'Publicações científicas'
        ordering = ['ordem', 'titulo']

    def __unicode__(self):
        if self.titulo:
            return self.titulo
        else:
            return self.ordem
