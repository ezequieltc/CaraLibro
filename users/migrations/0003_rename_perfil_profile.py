# Generated by Django 4.0.1 on 2022-01-20 03:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_rename_foto_perfil_perfil_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Perfil',
            new_name='Profile',
        ),
    ]