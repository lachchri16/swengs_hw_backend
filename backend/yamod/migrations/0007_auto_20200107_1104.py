# Generated by Django 3.0.2 on 2020-01-07 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yamod', '0006_song_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.TextField(choices=[('r', 'Rock'), ('j', 'Jazz'), ('t', 'Techno'), ('k', 'Klassik')], max_length=1, null=True),
        ),
    ]