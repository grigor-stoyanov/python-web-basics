# Generated by Django 4.0.2 on 2022-02-16 14:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_employee_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='employee',
            name='egn',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.MaxLengthValidator(10)], verbose_name='EGN'),
        ),
    ]
