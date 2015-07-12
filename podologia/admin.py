# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Servico, Historico, Podologo, Paciente, Anamnese, Atendimento, ServicoAtendimento, ObservacaoPaciente

class AnamneseInline(admin.TabularInline):
	model = Anamnese
	extra = 3

class ObservacaoPacienteInline(admin.StackedInline):
	model = ObservacaoPaciente
	extra = 1

class PacienteAdmin(admin.ModelAdmin):
	inlines = [AnamneseInline, ObservacaoPacienteInline]

class ServicoAtendimentoInline(admin.TabularInline):
	model = ServicoAtendimento
	extra = 1

class AtendimentoAdmin(admin.ModelAdmin):
	inlines = [ServicoAtendimentoInline]

admin.site.register(Servico)
admin.site.register(Historico)
admin.site.register(Podologo)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Atendimento, AtendimentoAdmin)