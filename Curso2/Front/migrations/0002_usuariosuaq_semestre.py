# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Front', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariosuaq',
            name='semestre',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
