# Generated by Django 3.2.25 on 2024-10-08 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtgfinance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='eur_price',
        ),
        migrations.RemoveField(
            model_name='card',
            name='tix_price',
        ),
    ]
