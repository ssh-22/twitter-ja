# Generated by Django 2.2 on 2019-06-28 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0004_auto_20190624_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='accounts.Account', verbose_name='ユーザーID'),
        ),
    ]