# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anamnese',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quando', models.DateTimeField(default=datetime.datetime.now)),
                ('observacao', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pessoa', models.ForeignKey(to='administrativo.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Podologo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pessoa', models.ForeignKey(to='administrativo.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='ServicoAtendimento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('preco', models.DecimalField(max_digits=10, decimal_places=2)),
                ('atendimento', models.ForeignKey(to='podologia.Atendimento')),
                ('servico', models.ForeignKey(to='podologia.Servico')),
            ],
        ),
        migrations.AddField(
            model_name='atendimento',
            name='paciente',
            field=models.ForeignKey(to='podologia.Paciente'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='podologo',
            field=models.ForeignKey(to='podologia.Podologo'),
        ),
        migrations.AddField(
            model_name='anamnese',
            name='historico',
            field=models.ForeignKey(to='podologia.Historico'),
        ),
        migrations.AddField(
            model_name='anamnese',
            name='paciente',
            field=models.ForeignKey(to='podologia.Paciente'),
        ),
    ]
