# Generated by Django 4.2.4 on 2023-09-08 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centers', '0007_remove_requesttour_time_requesttour_times_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='image',
        ),
        migrations.AddField(
            model_name='employee',
            name='employeeImage',
            field=models.ImageField(default='1.png', upload_to='images/'),
        ),
    ]
