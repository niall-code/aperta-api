# Generated by Django 3.2.23 on 2024-11-18 16:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reports', '0006_auto_20241118_1100'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='report',
            unique_together={('owner', 'post_id')},
        ),
        migrations.RemoveField(
            model_name='report',
            name='reported_post',
        ),
    ]
