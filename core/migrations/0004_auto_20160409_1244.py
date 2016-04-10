# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_category_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('family', models.CharField(max_length=50, verbose_name=b'Family')),
                ('photo', models.ImageField(upload_to=b'people', verbose_name=b'Photo', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email', blank=True)),
            ],
            options={
                'db_table': 'person',
            },
        ),
        migrations.RemoveField(
            model_name='news',
            name='posted',
        ),
        migrations.RemoveField(
            model_name='news',
            name='short_tile',
        ),
        migrations.AddField(
            model_name='news',
            name='source',
            field=models.CharField(default='', max_length=70, verbose_name=b'Source'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='sub_title',
            field=models.CharField(default='', unique=True, max_length=255),
            preserve_default=False,
        ),
    ]
