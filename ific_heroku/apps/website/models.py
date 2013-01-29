# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

class SalaImprensaDestaqueManager(models.Manager):
    def get_query_set(self):
        return super(SalaImprensaDestaqueManager, self).get_query_set().filter(destaque=True)

# Create your models here.
class SalaImprensa(models.Model):
    titulo = models.CharField(u'Título', max_length=120)
    slug = models.SlugField(max_length=120, null=True, blank=True)
    data_pub = models.DateTimeField(u'Data de publicação', auto_now_add=True)
    subtitulo = models.CharField(u'Subtítulo', max_length=120, null=True, blank=True)
    video = models.TextField(u'Vídeo', null=True, blank=True)
    texto = models.TextField('Texto', null=True, blank=True)
    link = models.CharField(u'Link', max_length=120, null=True, blank=True)
    foto = models.ImageField('Foto', upload_to='images/sala_imprensa', null=True, blank=True)
    destaque = models.BooleanField(default=False)

    # Manager
    objects = models.Manager()
    destaques = SalaImprensaDestaqueManager()

    class Meta:
        db_table = 'website_salaimprensa'
        verbose_name = u'Sala de imprensa'
        verbose_name_plural = u'Salas de imprensa'
        ordering = ['-data_pub']

    @models.permalink
    def get_absolute_url(self):
        return ('core:noticia', None, {
                'year': str(self.data_pub.year),
                'month': str(self.data_pub.month).zfill(2),
                'day': str(self.data_pub.day).zfill(2),
                'slug': str(self.slug),
            }
        )

    def __unicode__(self):
        return self.titulo


@receiver(pre_save, sender=SalaImprensa)
def save_slug_sala_imprensa(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(sender.titulo)


class Equipe(models.Model):
    ordem = models.PositiveSmallIntegerField(default=0)
    nome = models.CharField('Nome', max_length=120)
    resumo = models.TextField(u'Resumo do currículo')
    email = models.EmailField('Email', null=True, blank=True)
    site = models.URLField('Site', verify_exists=False, null=True, blank=True)
    foto = models.ImageField('Foto do colaborador', upload_to='images/equipe', null=True, blank=True)
    data_pub = models.DateTimeField(u'Data de publicação', auto_now_add=True)
    
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
    thumb = models.ImageField('Thumb', upload_to='images/gallery', null=True, blank=True)
    texto = models.TextField(u'Subtítulo da foto', null=True, blank=True)
    data_pub = models.DateTimeField(u'Data de publicação', auto_now_add=True)

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
