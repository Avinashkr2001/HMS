# Generated by Django 5.0.6 on 2024-06-23 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_rename_username_doctor_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='Phone',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='doctor',
            name='Specility',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_id',
            field=models.CharField(default='', max_length=50),
        ),
    ]
