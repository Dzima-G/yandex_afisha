# Generated by Django 4.2.17 on 2025-02-18 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_alter_image_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='description_long',
            new_name='long_description',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='description_short',
            new_name='short_description',
        ),
    ]
