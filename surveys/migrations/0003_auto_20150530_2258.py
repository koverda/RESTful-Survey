# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_auto_20150530_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='feedback',
            field=models.CharField(default=b'', max_length=500, verbose_name=b'Would you like to provide any other feedback?', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='survey',
            name='recommend_company',
            field=models.CharField(max_length=2, verbose_name=b'How likely would you be to recommend this company to a friend?', choices=[(b'1', b'1 - Very Unlikely'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10 - Very Likely')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='survey',
            name='was_researched',
            field=models.BooleanField(verbose_name=b'Did you research the product before purchasing it?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='survey',
            name='what_changes',
            field=models.CharField(default=b'', max_length=500, verbose_name=b'What would you change about the product?'),
            preserve_default=True,
        ),
    ]
