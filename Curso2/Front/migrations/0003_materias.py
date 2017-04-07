# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Front', '0002_usuariosuaq_semestre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parciales', models.IntegerField()),
                ('nombre_materia', models.CharField(max_length=100)),
                ('veces_cursadas', models.IntegerField()),
                ('cuenta_temario', models.BooleanField()),
                ('semestre', models.IntegerField()),
                ('obligatorio', models.BooleanField()),
            ],
        ),
    ]
