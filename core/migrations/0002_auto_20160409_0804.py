# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'news'},
        ),
        migrations.AddField(
            model_name='news',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 9, 8, 4, 44, 395706), verbose_name=b'Added Date', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='date_modify',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 9, 8, 4, 51, 52779), verbose_name=b'Modified Date', auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]
