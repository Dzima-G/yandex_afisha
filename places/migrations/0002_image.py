# Generated by Django 4.2.17 on 2024-12-14 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geeks_field', models.PositiveIntegerField(verbose_name='Расположение')),
                ('image', models.ImageField(upload_to='', verbose_name='Картинка')),
                ('palace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.place', verbose_name='Место')),
            ],
        ),
    ]