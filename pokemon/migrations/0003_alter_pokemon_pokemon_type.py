# Generated by Django 4.0.4 on 2022-07-19 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_alter_pokemon_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='Pokemon_Type',
            field=models.CharField(choices=[("('WATER', 'WA')", 'Water'), ("('GRASS', 'GR')", 'Grass'), ("('GHOST', 'GH')", 'Ghost'), ("('STEEL', 'ST')", 'Steel'), ("('FAIRY', 'FA')", 'Fariy')], max_length=200),
        ),
    ]
