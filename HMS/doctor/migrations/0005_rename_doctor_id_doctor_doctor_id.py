# Generated by Django 5.0.6 on 2024-06-25 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_doctor_joining_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='doctor_id',
            new_name='Doctor_id',
        ),
    ]
