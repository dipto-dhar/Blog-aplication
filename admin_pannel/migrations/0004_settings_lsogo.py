# Generated by Django 5.0.6 on 2024-07-03 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_pannel', '0003_alter_post_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='lsogo',
            field=models.ImageField(default=True, upload_to='site_images/'),
        ),
    ]