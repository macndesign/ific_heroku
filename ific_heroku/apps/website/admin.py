from django.contrib import admin
from apps.website.models import SalaImprensa, Equipe, Galeria
from apps.website.models import PublicacaoCientifica

class SalaImprensaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data_pub']
    prepopulated_fields = {"slug": ('titulo',)}

    class Meta:
        ordering = ['-data_pub']

admin.site.register(SalaImprensa, SalaImprensaAdmin)

class EquipeAdmin(admin.ModelAdmin):
    list_editable = ['ordem']
    list_display_links = ['nome', 'data_pub']
    list_display = ['ordem', 'nome', 'data_pub', 'email']
    class Meta:
        ordering = ['ordem']

admin.site.register(Equipe, EquipeAdmin)

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ['ordem', 'texto', 'data_pub']
    class Meta:
        ordering = ['ordem']

admin.site.register(Galeria, GaleriaAdmin)

class PublicacaoCientificaAdmin(admin.ModelAdmin):
    pass

admin.site.register(PublicacaoCientifica, PublicacaoCientificaAdmin)
