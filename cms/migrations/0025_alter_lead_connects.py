# Generated by Django 5.1 on 2024-11-18 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0024_rename_content_note_note_note_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='connects',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
