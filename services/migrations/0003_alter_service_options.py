# Generated by Django 4.0.4 on 2022-05-31 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_rename_update_at_service_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-created_at', 'updated_at'], 'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
    ]