# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('recommend_company', models.CharField(max_length=2, verbose_name=b'How likely would you be to recommend this company to a friend?', choices=[(b'1', b'1 - Very Unlikely'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10 - Very Likely')])),
                ('what_changes', models.CharField(default=b'', max_length=500, verbose_name=b'What would you change about the product?')),
                ('was_researched', models.BooleanField(default=True, verbose_name=b'Did you research the product before purchasing it?', choices=[(True, b'Yes'), (False, b'No')])),
                ('feedback', models.CharField(default=b'', max_length=500, verbose_name=b'Would you like to provide any other feedback?', blank=True)),
                ('owner', models.ForeignKey(related_name='surveys', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
    ]
