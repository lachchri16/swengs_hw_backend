# Generated by Django 3.0.2 on 2020-01-06 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yamod', '0004_auto_20200106_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.DurationField(null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]
