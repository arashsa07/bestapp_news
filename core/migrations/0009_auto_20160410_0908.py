# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20160410_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='name',
            field=models.CharField(unique=True, max_length=50, verbose_name=b'Agency Name'),
        ),
    ]
