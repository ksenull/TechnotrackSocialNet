# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0002_chat_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]