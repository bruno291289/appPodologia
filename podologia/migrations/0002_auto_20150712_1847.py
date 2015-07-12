# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podologia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObservacaoPaciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=250)),
                ('quando', models.DateTimeField(auto_now_add=True)),
                ('pessoa', models.ForeignKey(to='podologia.Paciente')),
            ],
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='descricao',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='observacao',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
