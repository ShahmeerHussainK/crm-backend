# Generated by Django 5.1 on 2024-10-30 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_profile_gender_alter_profile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Division Lead', 'Division Lead'), ('HR', 'HR'), ('BD', 'BD'), ('Employee', 'Employee'), ('Project Manager', 'Project Manager'), ('IT', 'IT')], default='Employee', max_length=20),
        ),
    ]