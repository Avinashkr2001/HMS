# Generated by Django 5.0.6 on 2024-06-25 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_appointment_appointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='Appointment_date',
            field=models.CharField(default=datetime.datetime(2024, 6, 25, 13, 12, 40, 845458, tzinfo=datetime.timezone.utc), max_length=50),
        ),
    ]
