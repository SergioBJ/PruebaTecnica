# Generated by Django 4.2.11 on 2024-04-08 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employee_job_functions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
