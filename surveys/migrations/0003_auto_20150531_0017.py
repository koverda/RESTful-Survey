# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_survey_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='was_researched',
            field=models.BooleanField(default=True, verbose_name=b'Did you research the product before purchasing it?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
    ]
