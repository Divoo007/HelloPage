# Generated by Django 3.2.4 on 2022-02-03 14:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_hpuser_file1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hpuser',
            name='file1',
        ),
        migrations.AddField(
            model_name='contact',
            name='tahash',
            field=models.TextField(default=django.utils.timezone.now, max_length=4096),
            preserve_default=False,
        ),
    ]