# Generated by Django 4.2 on 2023-05-01 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roster',
            name='school',
        ),
    ]
