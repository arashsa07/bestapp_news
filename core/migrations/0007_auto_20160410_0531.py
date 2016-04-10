# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_news_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Agency Name')),
            ],
            options={
                'db_table': 'agencies',
            },
        ),
        migrations.AlterField(
            model_name='news',
            name='writer',
            field=models.ForeignKey(related_name='news_writer', to='core.Person'),
        ),
    ]
