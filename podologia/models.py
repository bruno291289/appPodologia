# -*- coding: utf-8 -*-
from django.db import models
import administrativo
from datetime import datetime

class Servico(models.Model):
	nome = models.CharField(max_length=100)
	preco = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.nome

class Historico(models.Model):
	nome = models.CharField(max_length=100)

	def __str__(self):
		return self.nome

class Podologo(models.Model):
	pessoa = models.ForeignKey('administrativo.Pessoa')

	def __str__(self):
		return self.pessoa.nome

class Paciente(models.Model):
	pessoa = models.ForeignKey('administrativo.Pessoa')

	def __str__(self):
		return self.pessoa.nome

class Anamnese(models.Model):
	paciente = models.ForeignKey(Paciente)
	historico = models.ForeignKey(Historico)
	descricao = models.CharField(max_length=250, blank=True, null=True)

	def __str__(self):
		return self.historico.nome + " - " + self.descricao

class Atendimento(models.Model):
	podologo = models.ForeignKey(Podologo)
	paciente = models.ForeignKey(Paciente)
	quando = models.DateTimeField(default=datetime.now)
	observacao = models.CharField(max_length=500, blank=True, null=True)

	def __str__(self):
		return "Atendimento de " + self.paciente.pessoa.nome + " feito por " + self.podologo.pessoa.nome + " em " + self.quando.strftime('%Y-%m-%d %H:%M');

class ServicoAtendimento(models.Model):
	atendimento = models.ForeignKey(Atendimento)
	servico = models.ForeignKey(Servico)
	preco = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.servico.nome

class ObservacaoPaciente(models.Model):
	pessoa = models.ForeignKey(Paciente)
	descricao = models.CharField(max_length=250)
	quando = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.descricao