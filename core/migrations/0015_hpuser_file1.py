# Generated by Django 3.2.4 on 2021-11-18 14:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_signup_pagename'),
    ]

    operations = [
        migrations.AddField(
            model_name='hpuser',
            name='file1',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]