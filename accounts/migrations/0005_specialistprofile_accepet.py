# Generated by Django 4.2.4 on 2023-09-10 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_specialistprofile_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialistprofile',
            name='accepet',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
