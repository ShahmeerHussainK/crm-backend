# Generated by Django 5.1 on 2024-08-28 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_skill_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
