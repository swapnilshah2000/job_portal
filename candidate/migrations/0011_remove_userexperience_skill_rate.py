# Generated by Django 4.2 on 2023-04-28 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0010_remove_userskill_skill_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userexperience',
            name='skill_rate',
        ),
    ]
