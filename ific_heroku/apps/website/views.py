# -*- coding: utf-8 -*-
# Create your views here.
from django.core.mail import send_mail
from django.core.paginator import InvalidPage, EmptyPage, Paginator
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from apps.website.forms import FaleConoscoForm
from apps.website.models import Galeria, Equipe, PublicacaoCientifica, SalaImprensa

def sobre(request):
    destaques = SalaImprensa.objects.filter(destaque=True)
    context = {
        'destaques': destaques,
        }
    return render_to_response(
        'website/sobre-o-ific.html',
        context,
        RequestContext(request)
    )

def galeria(request):
    items = Galeria.objects.all()
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
        'website/galeria.html',
        {'items': items},
        context_instance=RequestContext(request)
    )


def equipe(request):
    items = Equipe.objects.all()
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
        'website/equipe.html',
        {'items': items},
        context_instance=RequestContext(request)
    )


def publicacao_cientifica(request):
    items = PublicacaoCientifica.objects.all()
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
        'website/publicacao-cientifica.html',
        {'items': items},
        context_instance=RequestContext(request)
    )


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
            send_mail(subject, body, from_email, ['contato@ific.org.br'], fail_silently=False)

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
