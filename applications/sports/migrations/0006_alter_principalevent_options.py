# Generated by Django 4.2.4 on 2024-02-25 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0005_principalevent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='principalevent',
            options={'verbose_name': 'Evento Principal', 'verbose_name_plural': 'Eventos principales'},
        ),
    ]
