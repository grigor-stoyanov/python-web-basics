# Generated by Django 4.0.1 on 2022-01-28 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0008_alter_employee_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='job_title',
            field=models.CharField(choices=[(1, 'Software Developer'), (2, 'QA Engineer'), (3, 'Dev Ops Specialist')], default=1, max_length=20),
        ),
    ]