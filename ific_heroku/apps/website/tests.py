# coding: utf-8
"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse as r

class SobreIFICTest(TestCase):
    fixtures = ['website_testdata.json']

    def setUp(self):
        self.resp = self.client.get(r('core:sobre'))

    def test_get(self):
        """O Método GET tem que retornar o código 200"""
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        """A página Sobre o IFIC usa o template sobre-o-ific.html"""
        self.assertTemplateUsed(self.resp, 'website/sobre-o-ific.html')

    def test_destaques(self):
        """Verifica se todos os destaques estão na tela"""
        self.assertContains(self.resp, 'Faltam doadores')
        self.assertContains(self.resp, 'Equipe do Transplante')
        self.assertNotContains(self.resp, 'Assembleia Legislativa do Estado')

    def test_links_topmenu(self):
        """Verificando se existem todos os links necessários no menu do topo"""
        self.assertContains(self.resp, 'href="{0}">Home</a>'.format(r('core:sobre')))
        self.assertContains(self.resp, 'href="{0}">Missão</a>'.format(r('core:missao')))
        self.assertContains(self.resp, 'href="{0}">Projetos</a>'.format(r('core:projetos')))
        self.assertContains(self.resp, 'href="{0}">Diagnóstico</a>'.format(r('core:transplante-diagnostico')))
        self.assertContains(self.resp, 'href="{0}">Cirurgia</a>'.format(r('core:transplante-cirurgia')))
        self.assertContains(self.resp, 'href="{0}">Pós-operatório</a>'.format(r('core:transplante-pos-operatorio')))
        self.assertContains(self.resp, 'href="{0}">Histórias de vida</a>'.format(r('core:transplante-historias-de-vida')))
        self.assertContains(self.resp, 'href="{0}">Doenças Hepáticas</a>'.format(r('core:prevencao-doencas-hepaticas')))
        self.assertContains(self.resp, 'href="{0}">Alcoolismo</a>'.format(r('core:prevencao-alcoolismo')))
        self.assertContains(self.resp, 'href="{0}">Poluentes Ambientais</a>'.format(r('core:prevencao-poluentes-ambientais')))
        self.assertContains(self.resp, 'href="{0}">Alimentação e Sedentarismo</a>'.format(r('core:prevencao-alimentacao-e-sedentarismo')))
        self.assertContains(self.resp, 'href="{0}">Medicamentos</a>'.format(r('core:prevencao-medicamentos')))

    def test_links_sidebar(self):
        """Verificando se existem todos os links necessários no menu lateral"""
        self.assertContains(self.resp, 'href="{0}">Como apoiar o IFIC</a>'.format(r('core:como-apoiar')))
        self.assertContains(self.resp, 'href="{0}">Seja um doador de órgãos</a>'.format(r('core:seja-um-doador')))
        self.assertContains(self.resp, 'href="{0}">Galeria</a>'.format(r('core:galeria')))
        self.assertContains(self.resp, 'href="{0}">Equipe</a>'.format(r('core:equipe')))
        self.assertContains(self.resp, 'href="{0}">Notícias</a>'.format(r('core:noticias')))
        self.assertContains(self.resp, 'href="{0}">Fale conosco</a>'.format(r('core:fale-conosco')))
        self.assertContains(self.resp, 'href="{0}">Publicações Científicas</a>'.format(r('core:publicacao-cientifica')))
