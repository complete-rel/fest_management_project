# Generated by Django 5.1.6 on 2025-03-05 19:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default='18:00:00'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default='12:00:00'),
        ),
    ]
