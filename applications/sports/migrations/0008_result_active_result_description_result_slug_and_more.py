# Generated by Django 4.2.4 on 2024-02-29 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0007_events_slug_principalevent_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Activo'),
        ),
        migrations.AddField(
            model_name='result',
            name='description',
            field=models.TextField(blank=True, verbose_name='descripcion'),
        ),
        migrations.AddField(
            model_name='result',
            name='slug',
            field=models.CharField(blank=True, max_length=180, null=True, unique=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='result',
            name='sport',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sports.sports'),
            preserve_default=False,
        ),
    ]
