# Generated by Django 5.0.6 on 2024-07-03 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_pannel', '0005_rename_lsogo_settings_fav_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='fav_icon',
            field=models.ImageField(upload_to='site_images/'),
        ),
    ]
