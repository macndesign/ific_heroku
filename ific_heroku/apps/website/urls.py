# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('',

    # -*- Top Menu -*-

    # Sobre
    url(r'^$', 'apps.website.views.sobre', name='sobre'),

    # Missão
    url(r'^missao/$', 'django.views.generic.simple.direct_to_template',
            {'template': 'website/missao.html'}, name='missao'),

    # Projetos
    url(r'^projetos/$', 'django.views.generic.simple.direct_to_template',
            {'template': 'website/projetos.html'}, name='projetos'),

    # Transplante
    url(r'^transplante/diagnostico/$', 'django.views.generic.simple.direct_to_template',
            {'template': 'website/transplante-diagnostico.html'}, name='transplante-diagnostico'),
    url(r'^transplante/cirurgia/$', 'django.views.generic.simple.direct_to_template',
            {'template': 'website/transplante-cirurgia.html'}, name='transplante-cirurgia'),
    url(r'^transplante/pos-operatorio/$', 'django.views.generic.simple.direct_to_template',
            {'template': 'website/transplante-pos-operatorio.html'}, name='transplante-pos-operatorio'),
    url(r'^transplante/historias-de-vida/$', 'django.views.generic.simple.direct_to_template',
            {'template': 'website/transplante-historias-de-vida.html'}, name='transplante-historias-de-vida'),

    # Prevenção
    url(r'^prevencao/doencas-hepaticas/$', 'django.views.generic.simple.direct_to_template',
            {'template': 'website/prevencao-doencas-hepaticas.html'}, name='prevencao-doencas-hepaticas'),
    url(r'^prevencao/alcoolismo/$', 'django.views.generic.simple.direct_to_template',
            {'template': 'website/prevencao-alcoolismo.html'}, name='prevencao-alcoolismo'),
    url(r'^prevencao/poluentes-ambientais/$', 'django.views.generic.simple.direct_to_template',
            {'template': 'website/prevencao-poluentes-ambientais.html'}, name='prevencao-poluentes-ambientais'),
    url(r'^prevencao/alimentacao-e-sedentarismo/$', 'django.views.generic.simple.direct_to_template',
            {'template': 'website/prevencao-alimentacao-e-sedentarismo.html'}, name='prevencao-alimentacao-e-sedentarismo'),
    url(r'^prevencao/medicamentos/$', 'django.views.generic.simple.direct_to_template',
            {'template': 'website/prevencao-medicamentos.html'}, name='prevencao-medicamentos'),

    # -*- Side bar -*-

    # Como apoiar o IFIC
    url(r'^como-apoiar/$', 'django.views.generic.simple.direct_to_template',
            {'template': 'website/como-apoiar.html'}, name='como-apoiar'),

    # Seja um doador
    url(r'^seja-um-doador/$', 'django.views.generic.simple.direct_to_template',
            {'template': 'website/seja-um-doador.html'}, name='seja-um-doador'),

    # Galeria
    url(r'^galeria/$', 'apps.website.views.galeria', name='galeria'),

    # Equipe
    url(r'^equipe/$', 'apps.website.views.equipe', name='equipe'),

    # Fale conosco
    url(r'^fale-conosco/$', 'apps.website.views.fale_conosco', name='fale-conosco'),

    # Publicações científicas
    url(r'^publicacao-cientifica/$', 'apps.website.views.publicacao_cientifica', name='publicacao-cientifica'),

    # Notícias
    url(r'^noticias/$', 'apps.website.views.noticias', name='noticias'),
    url(r'^noticia/(?P<year>\d{4})/(?P<month>[0-9]{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'apps.website.views.noticia', name='noticia'),
)
