# Generated by Django 4.0.1 on 2022-01-28 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0006_testmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='job_title',
            field=models.CharField(choices=[('Software Developer', 1), ('QA Engineer', 2), ('Dev Ops Specialist', 3)], default='', max_length=20),
            preserve_default=False,
        ),
    ]
