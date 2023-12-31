# Generated by Django 4.2.5 on 2023-09-08 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_detection_crop_loc_alter_detection_pred_loc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detection',
            name='crop_json_base64',
        ),
        migrations.RemoveField(
            model_name='detection',
            name='pred_json_base64',
        ),
        migrations.AlterField(
            model_name='detection',
            name='processing_time_ocr',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='detection',
            name='processing_time_pred',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=30, null=True),
        ),
    ]
