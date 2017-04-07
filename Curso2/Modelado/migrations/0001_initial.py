# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Platillo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_platillo', models.CharField(max_length=100)),
                ('descripcion_platillo', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('porcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('numero_mesas', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('horario', models.CharField(max_length=100)),
                ('calificacion', models.IntegerField(default=10)),
            ],
        ),
        migrations.AddField(
            model_name='platillo',
            name='restaurante',
            field=models.ForeignKey(to='Modelado.Restaurante'),
        ),
    ]
