# Generated by Django 3.0.2 on 2020-01-07 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yamod', '0005_auto_20200106_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.TextField(default='NaN'),
            preserve_default=False,
        ),
    ]
