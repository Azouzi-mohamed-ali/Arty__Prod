# Generated by Django 4.1.7 on 2023-05-19 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProd', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
    ]