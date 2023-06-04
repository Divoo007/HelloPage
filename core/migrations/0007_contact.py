# Generated by Django 3.2.4 on 2021-08-21 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_hpuser_pagename'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=128)),
                ('phone', models.CharField(max_length=16)),
                ('subject', models.CharField(max_length=512)),
                ('text', models.CharField(max_length=4096)),
            ],
        ),
    ]