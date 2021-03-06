# Generated by Django 4.0.1 on 2022-01-28 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0015_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=254)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee_app.employee')),
            ],
        ),
    ]
