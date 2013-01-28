# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from apps.website.views import *

urlpatterns = patterns('',

    # -*- Top Menu -*-

    # Sobre
    url(r'^$', SobreListView.as_view(), name='sobre'),

    # Missão
    url(r'^missao/$', MissaoTemplateView.as_view(), name='missao'),

    # Projetos
    url(r'^projetos/$', ProjetosTemplateView.as_view(), name='projetos'),

    # Transplante
    url(r'^transplante/diagnostico/$', TransplateDiagnosticoTemplateView.as_view(), name='transplante-diagnostico'),
    url(r'^transplante/cirurgia/$', TransplateCirurgiaTemplateView.as_view(), name='transplante-cirurgia'),
    url(r'^transplante/pos-operatorio/$', TransplantePosOperatorioTemplateView.as_view(), name='transplante-pos-operatorio'),
    url(r'^transplante/historias-de-vida/$', TransplanteHistoriasVidaTemplateView.as_view(), name='transplante-historias-de-vida'),

    # Prevenção
    url(r'^prevencao/doencas-hepaticas/$', PrevencaoDoencasHepaticasTemplateView.as_view(), name='prevencao-doencas-hepaticas'),
    url(r'^prevencao/alcoolismo/$', PrevencaoAlcoolismoTemplateView.as_view(), name='prevencao-alcoolismo'),
    url(r'^prevencao/poluentes-ambientais/$', PrevencaoPoluentesAmbientaisTemplateView.as_view(), name='prevencao-poluentes-ambientais'),
    url(r'^prevencao/alimentacao-e-sedentarismo/$', PrevencaoAlimentacaoSedentarismoTemplateView.as_view(), name='prevencao-alimentacao-e-sedentarismo'),
    url(r'^prevencao/medicamentos/$', PrevencaoMedicamentosTemplateView.as_view(), name='prevencao-medicamentos'),

    # -*- Side bar -*-

    # Como apoiar o IFIC
    url(r'^como-apoiar/$', ComoApoiarTemplateView.as_view(), name='como-apoiar'),

    # Seja um doador
    url(r'^seja-um-doador/$', SejaDoadorTemplateView.as_view(), name='seja-um-doador'),

    # Galeria
    url(r'^galeria/$', GaleriaListView.as_view(), name='galeria'),

    # Equipe
    url(r'^equipe/$', EquipeListView.as_view(), name='equipe'),

    # Notícias
    url(r'^noticias/$', NoticiaListView.as_view(), name='noticias'),
    # url(r'^noticia/(?P<year>\d{4})/(?P<month>[0-9]{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'apps.website.views.noticia', name='noticia'),
    url(r'^noticia/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[-\w]+)/(?P<pk>\d+)/$', NoticiaDateDetailView.as_view(), name="noticia"),

    # Fale conosco
    url(r'^fale-conosco/$', 'apps.website.views.fale_conosco', name='fale-conosco'),

    # Publicações científicas
    url(r'^publicacao-cientifica/$', PublicacaoCientificaListView.as_view(), name='publicacao-cientifica'),
)
