# Generated by Django 3.2.4 on 2021-11-08 15:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_rename_block_data_block_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='pagename',
            field=models.CharField(default=django.utils.timezone.now, max_length=128, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
