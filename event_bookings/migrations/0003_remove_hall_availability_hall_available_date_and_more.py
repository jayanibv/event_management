# Generated by Django 5.1.2 on 2024-10-30 05:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("event_bookings", "0002_rename_is_available_hall_availability"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="hall",
            name="availability",
        ),
        migrations.AddField(
            model_name="hall",
            name="available_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="hall",
            name="available_time",
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="hall",
            name="event_type",
            field=models.CharField(default="General", max_length=50),
        ),
    ]