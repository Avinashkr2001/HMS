# Generated by Django 5.0.6 on 2024-06-19 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms_admin', '0002_rename_admin_details_admin_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_detail',
            name='admin_username',
            field=models.CharField(default='hms_admin123', max_length=50),
        ),
    ]
