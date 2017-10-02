# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0002_remove_ninjas_dojo_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ninjas',
            name='dojo_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dojo_ninjas.dojos'),
        ),
    ]
