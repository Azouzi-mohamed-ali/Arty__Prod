# Generated by Django 4.1.7 on 2023-05-21 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProd', '0004_demande_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='demande',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
    ]
