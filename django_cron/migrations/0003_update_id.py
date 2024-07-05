# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_cron', '0002_remove_max_length_from_CronJobLog_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cronjoblog',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
