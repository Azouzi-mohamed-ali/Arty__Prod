# Generated by Django 4.1.7 on 2023-05-21 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProd', '0002_remove_contact_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='demande',
            fields=[
                ('client_name', models.CharField(max_length=50, null=True)),
                ('number_client', models.CharField(max_length=50, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Partenaire',
        ),
    ]
