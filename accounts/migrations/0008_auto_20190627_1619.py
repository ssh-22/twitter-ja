# Generated by Django 2.2 on 2019-06-27 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20190627_1544'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='relationship',
            unique_together={('following_id', 'follower_id', 'updated_at')},
        ),
    ]
