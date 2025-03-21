# Generated by Django 5.1.6 on 2025-02-27 20:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('venues', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('tickets_available', models.PositiveIntegerField()),
                ('volunteers_needed', models.PositiveIntegerField(default=0)),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='venues.venue')),
            ],
        ),
    ]
