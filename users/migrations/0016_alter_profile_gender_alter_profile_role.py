# Generated by Django 5.1 on 2024-10-24 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_remove_workexperience_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Not Prefer', 'Not Prefer')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Division Lead', 'Division Lead'), ('HR', 'HR'), ('BD', 'BD'), ('Employee', 'Employee')], default='Employee', max_length=20),
        ),
    ]
