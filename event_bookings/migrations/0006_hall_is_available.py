# Generated by Django 5.1.2 on 2024-11-03 07:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("event_bookings", "0005_booking_booking_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="hall",
            name="is_available",
            field=models.BooleanField(default=True),
        ),
    ]
