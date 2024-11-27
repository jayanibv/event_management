# Generated by Django 5.1.2 on 2024-10-30 15:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("event_bookings", "0004_remove_hall_available_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="booking_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]