# Generated by Django 3.2.4 on 2021-08-19 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_recover'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='username',
            new_name='pagename',
        ),
        migrations.RemoveField(
            model_name='hpuser',
            name='username',
        ),
        migrations.AddField(
            model_name='hpuser',
            name='pagename',
            field=models.CharField(default='', max_length=128, unique=True),
            preserve_default=False,
        ),
    ]
