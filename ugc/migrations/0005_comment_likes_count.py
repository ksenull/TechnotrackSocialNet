# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0004_post_likes_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes_count',
            field=models.IntegerField(default=0),
        ),
    ]
