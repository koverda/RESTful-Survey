# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='was_researched',
            field=models.CharField(default=b'Yes', max_length=2, verbose_name=b'Did you research the product before purchasing it?', choices=[(1, b'Yes'), (0, b'No')]),
            preserve_default=True,
        ),
    ]
