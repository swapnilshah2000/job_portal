# Generated by Django 4.2 on 2023-04-27 15:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0006_alter_userproject_project_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercourse',
            name='currently_working',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usercourse',
            name='end_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='usercourse',
            name='start_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
