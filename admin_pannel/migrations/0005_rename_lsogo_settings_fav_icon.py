# Generated by Django 5.0.6 on 2024-07-03 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_pannel', '0004_settings_lsogo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settings',
            old_name='lsogo',
            new_name='fav_icon',
        ),
    ]
