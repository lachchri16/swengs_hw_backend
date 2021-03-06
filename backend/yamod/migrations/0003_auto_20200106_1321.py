# Generated by Django 3.0.2 on 2020-01-06 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yamod', '0002_auto_20200105_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='label',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yamod.Label'),
        ),
        migrations.AddField(
            model_name='label',
            name='headquarters',
            field=models.TextField(default='NaN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.ManyToManyField(blank=True, to='yamod.Artist'),
        ),
    ]
