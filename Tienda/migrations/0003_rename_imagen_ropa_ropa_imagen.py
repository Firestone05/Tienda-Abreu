# Generated by Django 4.0.4 on 2022-06-05 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0002_ropa_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ropa',
            old_name='imagen',
            new_name='ropa_imagen',
        ),
    ]
