# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 13:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import social.apps.django_app.default.fields


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0003_alter_email_max_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersocialauth',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_auth', to='ttusers.TTUser'),
        ),
    ]
