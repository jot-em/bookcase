# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-03 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0010_bookcategory_bookkind'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=200, null=True, verbose_name='Kategoria'),
        ),
        migrations.AlterField(
            model_name='book',
            name='kind',
            field=models.CharField(max_length=200, verbose_name='Rodzaj'),
        ),
    ]
