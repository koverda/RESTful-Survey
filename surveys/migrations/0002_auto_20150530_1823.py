# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('recommend_company', models.CharField(max_length=2, choices=[(b'1', b'1 - Very Unlikely'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10 - Very Likely')])),
                ('what_changes', models.CharField(default=b'', max_length=500)),
                ('was_researched', models.BooleanField()),
                ('feedback', models.CharField(default=b'', max_length=500, blank=True)),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Snippet',
        ),
    ]
