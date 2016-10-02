# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='contact',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
    ]
