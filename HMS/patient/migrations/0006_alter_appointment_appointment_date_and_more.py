# Generated by Django 5.0.6 on 2024-06-26 11:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0005_rename_department_appointment_disease_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='Appointment_date',
            field=models.CharField(default=datetime.datetime(2024, 6, 26, 11, 49, 51, 137761, tzinfo=datetime.timezone.utc), max_length=50),
        ),
        migrations.AlterField(
            model_name='patient_register',
            name='Image',
            field=models.ImageField(default='https://img.freepik.com/free-vector/user-circles-set_78370-4704.jpg?size=626&ext=jpg&ga=GA1.1.199161677.1717694373&semt=ais_user', upload_to='Image/'),
        ),
    ]
