# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-22 04:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0007_auto_20170921_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book_authors.Books'),
        ),
    ]
