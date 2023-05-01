# Generated by Django 4.2 on 2023-05-01 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_roster_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roster',
            name='position',
            field=models.CharField(choices=[('QB', 'Quarterback'), ('RB', 'Running Back'), ('FB', 'Fullback'), ('WR', 'Wide Receiver'), ('TE', 'Tight End'), ('OL', 'Offensive Line'), ('DL', 'Defensive Line'), ('LB', 'Linebacker'), ('CB', 'Cornerback'), ('S', 'Safety')], default='QB', max_length=2),
        ),
    ]
