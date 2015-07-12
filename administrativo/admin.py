# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Pais, Estado, Cidade, Pessoa, Endereco, Telefone, Email, ObservacaoPessoa

class EnderecoInline(admin.StackedInline):
	model = Endereco
	extra = 0

class TelefoneInline(admin.StackedInline):
	model = Telefone
	extra = 0

class EmailInline(admin.StackedInline):
	model = Email
	extra = 0

class ObservacaoPessoaInline(admin.StackedInline):
	model = ObservacaoPessoa
	extra = 0

class PessoaAdmin(admin.ModelAdmin):
	inlines = [EnderecoInline, TelefoneInline, EmailInline, ObservacaoPessoaInline]

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Cidade)