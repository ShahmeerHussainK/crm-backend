# Generated by Django 5.1 on 2024-08-28 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_developmentteam_project'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]