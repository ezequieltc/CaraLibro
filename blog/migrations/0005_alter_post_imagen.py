# Generated by Django 4.0.1 on 2022-01-23 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, height_field='url_height', upload_to='uploads', width_field='url_width'),
        ),
    ]
