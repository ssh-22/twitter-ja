# Generated by Django 2.2 on 2019-06-24 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0002_auto_20190624_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='timeline', verbose_name='ツイート画像'),
        ),
    ]