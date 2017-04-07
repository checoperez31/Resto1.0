# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Front', '0003_materias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materias',
            name='obligatorio',
            field=models.BooleanField(default=True),
        ),
    ]
