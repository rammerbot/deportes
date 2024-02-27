# Generated by Django 4.2.4 on 2024-02-26 17:07

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_video_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
                ('description', models.CharField(max_length=255, verbose_name='Descripcion')),
                ('image', models.ImageField(upload_to='publicidad/', verbose_name='Baner')),
                ('active', models.BooleanField(verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Publicidad',
                'verbose_name_plural': 'Publicidades',
            },
        ),
    ]
