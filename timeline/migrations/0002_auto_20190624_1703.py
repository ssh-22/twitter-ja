# Generated by Django 2.2 on 2019-06-24 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='picture',
            field=models.ImageField(null=True, upload_to='timeline', verbose_name='ツイート画像'),
        ),
    ]
