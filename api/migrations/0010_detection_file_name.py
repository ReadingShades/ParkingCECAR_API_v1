# Generated by Django 4.2.5 on 2023-09-08 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_detection_time_stamp_creation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detection',
            name='file_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
