# Generated by Django 4.2.5 on 2023-09-08 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_detection_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detection',
            name='time_stamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
