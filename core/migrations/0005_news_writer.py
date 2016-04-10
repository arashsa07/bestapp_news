# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160409_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='writer',
            field=models.ForeignKey(default=1, to='core.Person'),
            preserve_default=False,
        ),
    ]
