# Generated by Django 4.2.4 on 2023-09-10 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialists', '0002_remove_appointmentbooking_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentbooking',
            name='zoom_url',
            field=models.URLField(blank=True),
        ),
    ]