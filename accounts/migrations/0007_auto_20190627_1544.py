# Generated by Django 2.2 on 2019-06-27 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190627_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='total_followers',
        ),
        migrations.RemoveField(
            model_name='account',
            name='total_following',
        ),
    ]
