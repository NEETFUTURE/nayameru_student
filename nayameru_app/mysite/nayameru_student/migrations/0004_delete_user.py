# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-04 08:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nayameru_student', '0003_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]