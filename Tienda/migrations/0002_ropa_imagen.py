# Generated by Django 4.0.4 on 2022-06-04 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ropa',
            name='imagen',
            field=models.ImageField(null=True, upload_to='ropa'),
        ),
    ]
