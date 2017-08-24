# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-24 18:05
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JustShop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'categories'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category_slug',
            new_name='slug',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0.01)], verbose_name='\u0426\u0435\u043d\u0430, \u0440\u0443\u0431\u043b\u044c'),
        ),
    ]