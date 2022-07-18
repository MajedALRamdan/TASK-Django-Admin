# Generated by Django 4.0.4 on 2022-07-18 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Pokemon_Type', models.CharField(choices=[("('WATER', 'WA')", 'Water'), ("('GRASS', 'GR')", 'Grass'), ("('GHOST', 'GH')", 'Ghost'), ("('STEEL', 'ST')", 'Steel'), ("('FAIRY', 'FA')", 'Fariy')], max_length=200)),
                ('hp', models.PositiveBigIntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('name_fr', models.CharField(default='', max_length=30)),
                ('name_ar', models.CharField(default='', max_length=30)),
                ('name_jp', models.CharField(default='', max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
