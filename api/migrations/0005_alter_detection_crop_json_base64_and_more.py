# Generated by Django 4.2.5 on 2023-09-08 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_detection_crop_json_base64_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detection',
            name='crop_json_base64',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='detection',
            name='pred_json_base64',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
