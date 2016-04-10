# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20160410_0531'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agency',
            options={'verbose_name_plural': 'agencies'},
        ),
        migrations.AddField(
            model_name='category',
            name='agency',
            field=models.ForeignKey(default=1, to='core.Agency'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('agency', 'parent', 'title')]),
        ),
    ]
