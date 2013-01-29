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
        u'O Método GET tem que retornar o código 200'
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        u'A página Sobre o IFIC usa o template sobre-o-ific.html'
        self.assertTemplateUsed(self.resp, 'website/sobre-o-ific.html')

    def test_destaques(self):
        u'Verifica se todos os destaques estão na tela'
        self.assertContains(self.resp, 'Faltam doadores')
        self.assertContains(self.resp, 'Equipe do Transplante')
        self.assertNotContains(self.resp, 'Assembleia Legislativa do Estado')

    def test_links_topmenu(self):
        u'Verificando se existem todos os links necessários no menu do topo'
        self.assertContains(self.resp, 'href="{}">Home</a>'.format(r('core:sobre')))
        self.assertContains(self.resp, 'href="{}">Missão</a>'.format(r('core:missao')))
        self.assertContains(self.resp, 'href="{}">Projetos</a>'.format(r('core:projetos')))
        self.assertContains(self.resp, 'href="{}">Diagnóstico</a>'.format(r('core:transplante-diagnostico')))
        self.assertContains(self.resp, 'href="{}">Cirurgia</a>'.format(r('core:transplante-cirurgia')))
        self.assertContains(self.resp, 'href="{}">Pós-operatório</a>'.format(r('core:transplante-pos-operatorio')))
        self.assertContains(self.resp, 'href="{}">Histórias de vida</a>'.format(r('core:transplante-historias-de-vida')))
        self.assertContains(self.resp, 'href="{}">Doenças Hepáticas</a>'.format(r('core:prevencao-doencas-hepaticas')))
        self.assertContains(self.resp, 'href="{}">Alcoolismo</a>'.format(r('core:prevencao-alcoolismo')))
        self.assertContains(self.resp, 'href="{}">Poluentes Ambientais</a>'.format(r('core:prevencao-poluentes-ambientais')))
        self.assertContains(self.resp, 'href="{}">Alimentação e Sedentarismo</a>'.format(r('core:prevencao-alimentacao-e-sedentarismo')))
        self.assertContains(self.resp, 'href="{}">Medicamentos</a>'.format(r('core:prevencao-medicamentos')))

    def test_links_sidebar(self):
        u'Verificando se existem todos os links necessários no menu lateral'
        self.assertContains(self.resp, 'href="{}">Como apoiar o IFIC</a>'.format(r('core:como-apoiar')))
        self.assertContains(self.resp, 'href="{}">Seja um doador de órgãos</a>'.format(r('core:seja-um-doador')))
        self.assertContains(self.resp, 'href="{}">Galeria</a>'.format(r('core:galeria')))
        self.assertContains(self.resp, 'href="{}">Equipe</a>'.format(r('core:equipe')))
        self.assertContains(self.resp, 'href="{}">Notícias</a>'.format(r('core:noticias')))
        self.assertContains(self.resp, 'href="{}">Fale conosco</a>'.format(r('core:fale-conosco')))
        self.assertContains(self.resp, 'href="{}">Publicações Científicas</a>'.format(r('core:publicacao-cientifica')))
