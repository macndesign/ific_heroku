# -*- coding: utf-8 -*-
# Create your views here.
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from apps.website.forms import FaleConoscoForm
from apps.website.models import Galeria, Equipe, PublicacaoCientifica, SalaImprensa
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.dates import DateDetailView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

class SobreListView(ListView):
    queryset = SalaImprensa.objects.filter(destaque=True)
    template_name = 'website/sobre-o-ific.html'
    context_object_name = 'destaques'


class MissaoTemplateView(TemplateView):
    template_name = 'website/missao.html'


class ProjetosTemplateView(TemplateView):
    template_name = 'website/projetos.html'


class TransplateDiagnosticoTemplateView(TemplateView):
    template_name = 'website/transplante-diagnostico.html'


class TransplateCirurgiaTemplateView(TemplateView):
    template_name = 'website/transplante-cirurgia.html'


class TransplantePosOperatorioTemplateView(TemplateView):
    template_name = 'website/transplante-pos-operatorio.html'


class TransplanteHistoriasVidaTemplateView(TemplateView):
    template_name = 'website/transplante-historias-de-vida.html'


class PrevencaoDoencasHepaticasTemplateView(TemplateView):
    template_name = 'website/prevencao-doencas-hepaticas.html'


class PrevencaoAlcoolismoTemplateView(TemplateView):
    template_name = 'website/prevencao-alcoolismo.html'


class PrevencaoPoluentesAmbientaisTemplateView(TemplateView):
    template_name = 'website/prevencao-poluentes-ambientais.html'


class PrevencaoAlimentacaoSedentarismoTemplateView(TemplateView):
    template_name = 'website/prevencao-alimentacao-e-sedentarismo.html'


class PrevencaoMedicamentosTemplateView(TemplateView):
    template_name = 'website/prevencao-medicamentos.html'


class ComoApoiarTemplateView(TemplateView):
    template_name = 'website/como-apoiar.html'


class SejaDoadorTemplateView(TemplateView):
    template_name = 'website/seja-um-doador.html'


class GaleriaListView(ListView):
    model = Galeria
    template_name = 'website/galeria.html'
    paginate_by = 9


class EquipeListView(ListView):
    model = Equipe
    template_name = 'website/equipe.html'
    paginate_by = 9


class PublicacaoCientificaListView(ListView):
    model = PublicacaoCientifica
    template_name = 'website/publicacao-cientifica.html'
    paginate_by = 9


class NoticiaListView(ListView):
    model = SalaImprensa
    template_name = 'website/noticias.html'
    paginate_by = 9


class NoticiaDateDetailView(DateDetailView):
    model = SalaImprensa
    template_name = 'website/noticia.html'
    context_object_name = 'noticia'
    date_field = 'data_pub'
    year_format = '%Y'
    month_format = '%m'
    day_format = '%d'
    slug_field = 'slug'


class ContatoView(FormView):
    template_name = 'website/contato.html'
    form_class = FaleConoscoForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, u'Email enviado com sucesso.')
        return reverse_lazy('core:fale-conosco')

    def form_valid(self, form):
        form.send_mail()
        return super(ContatoView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, u'Formulário inválido.')
        return super(ContatoView, self).form_invalid(form)
