# Generated by Django 5.0.6 on 2024-06-22 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='username',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='password',
            new_name='Password',
        ),
    ]
