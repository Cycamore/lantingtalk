# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-05 12:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_article', '0006_remove_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_article.Category'),
        ),
    ]
