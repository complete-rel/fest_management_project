# Generated by Django 5.1.6 on 2025-03-05 19:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0002_volunteer_signup_date_volunteer_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='signup_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
