# Generated by Django 4.2.4 on 2023-09-08 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centers', '0010_rename_employee_name_centeremployee_employees_names'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
