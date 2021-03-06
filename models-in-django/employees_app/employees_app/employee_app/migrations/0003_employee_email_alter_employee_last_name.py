# Generated by Django 4.0.1 on 2022-01-28 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0002_employee_first_name_employee_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
