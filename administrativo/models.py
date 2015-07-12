# -*- coding: utf-8 -*-
from django.db import models

class Pais(models.Model):
	nome = models.CharField(max_length=100)

	def __str__(self):
		return self.nome

class Estado(models.Model):
	pais = models.ForeignKey(Pais)
	nome = models.CharField(max_length=100)

	def __str__(self):
		return self.nome

class Cidade(models.Model):
	estado = models.ForeignKey(Estado)
	nome = models.CharField(max_length=100)

	def __str__(self):
		return self.nome

class Pessoa(models.Model):
	nome = models.CharField(max_length=200)
	apelido = models.CharField(max_length=100,blank=True, null=True)

	def __str__(self):
		return self.nome

class Endereco(models.Model):
	pessoa = models.ForeignKey(Pessoa)
	cidade = models.ForeignKey(Cidade)
	rua = models.CharField(max_length=100)
	numero = models.IntegerField()
	bairro = models.CharField(max_length=100,blank=True, null=True)
	cep = models.CharField(max_length=8,blank=True, null=True)
	complemento = models.CharField(max_length=200,blank=True, null=True)

	def __str__(self):
		return self.rua

class Telefone(models.Model):
	pessoa = models.ForeignKey(Pessoa)
	numero = models.CharField(max_length=30)
	descricao = models.CharField(max_length=100,blank=True, null=True)

	def __str__(self):
		return self.numero

class Email(models.Model):
	pessoa = models.ForeignKey(Pessoa)
	email = models.CharField(max_length=100)
	descricao = models.CharField(max_length=100,blank=True, null=True)

	def __str__(self):
		return self.email

class ObservacaoPessoa(models.Model):
	pessoa = models.ForeignKey(Pessoa)
	descricao = models.CharField(max_length=250)
	quando = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.descricao