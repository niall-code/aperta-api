# Generated by Django 3.2.23 on 2024-11-18 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_auto_20241118_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='post_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
