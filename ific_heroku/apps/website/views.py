# -*- coding: utf-8 -*-
# Create your views here.
from django.core.mail import send_mail
from django.core.paginator import InvalidPage, EmptyPage, Paginator
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from apps.website.forms import FaleConoscoForm
from apps.website.models import Galeria, Equipe, PublicacaoCientifica, SalaImprensa
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

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


def noticias(request):
    items = SalaImprensa.objects.all()
    paginator = Paginator(items, 9)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        items = paginator.page(page)
    except (EmptyPage, InvalidPage):
        items = paginator.page(paginator.num_pages)

    return render_to_response(
        'website/noticias.html',
        {'items': items},
        context_instance=RequestContext(request)
    )


def noticia(request, year, month, day, slug):
    noticia = get_object_or_404(
        SalaImprensa,
        data_pub__year = year,
        data_pub__month = month,
        data_pub__day = day,
        slug = slug
    )
    context = {'noticia': noticia}
    return render_to_response(
        'website/noticia.html',
        context,
        RequestContext(request)
    )


def fale_conosco(request):
    form = FaleConoscoForm()

    if request.method == 'POST':
        form = FaleConoscoForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']
            body = u'Email: %s\nAssunto: %s\nMensagem: %s' % (from_email, subject, message)
            send_mail(subject, body, from_email, ['macndesign@gmail.com'], fail_silently=False)

            css_message = 'alert-success'
            alert_message = u'Email enviado!'
            context = {'form': form, 'message': alert_message, 'css_message': css_message}
            return render_to_response('website/fale-conosco.html', context, RequestContext(request))

        else:
            form = FaleConoscoForm(request.POST)
            css_message = 'alert-error'
            alert_message = u'Verifique os campos com erros de preenchimento.'
            context = {'form': form, 'message': alert_message, 'css_message': css_message}
            return render_to_response('website/fale-conosco.html', context, RequestContext(request))

    context = {'form': form}

    return render_to_response('website/fale-conosco.html', context, RequestContext(request))
