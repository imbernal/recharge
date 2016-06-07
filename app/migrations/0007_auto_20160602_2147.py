# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('money', models.CharField(max_length=250)),
                ('provider', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('item_number', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Transection',
        ),
    ]
