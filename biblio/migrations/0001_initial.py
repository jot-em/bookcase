# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-01 22:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200, verbose_name='Autor')),
                ('title', models.CharField(max_length=200, verbose_name='Tytuł')),
                ('kind', models.TextField(verbose_name='Gatunek')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data dodania')),
                ('loan_date', models.DateTimeField(blank=True, null=True, verbose_name='Data wypożyczenia')),
                ('due_date', models.DateTimeField(blank=True, null=True, verbose_name='Termin oddania')),
                ('category', models.CharField(default='Inne', max_length=200, verbose_name='Kategoria')),
                ('notes', models.TextField(blank=True, verbose_name='Notatki')),
            ],
        ),
    ]
