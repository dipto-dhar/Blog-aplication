# Generated by Django 5.0.6 on 2024-07-13 19:15

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_pannel', '0014_category_slug_post_slug_alter_contacts_purpose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='cat_name', unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]
