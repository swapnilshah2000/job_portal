# Generated by Django 4.2 on 2023-05-03 12:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_alter_job_datails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='datails',
            field=ckeditor.fields.RichTextField(default='\n<b>Tips:</b> Provide a summary of the role, what success in the position looks like, and how this role fits into the organization overall.<br>\n\n<b>Responsibilities</b>\n\n<p>[Be specific when describing each of the responsibilities. Use gender-neutral, inclusive language.]<br>\n\nExample: Determine and develop user requirements for systems in production, to ensure maximum usability</p>\n\n<b>Qualifications</b>\n\n<p>[Some qualifications you may want to include are Skills, Education, Experience, or Certifications.]<br>\n\nExample: Excellent verbal and written communication skills</p>\n'),
        ),
    ]
