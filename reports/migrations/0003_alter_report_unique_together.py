# Generated by Django 3.2.23 on 2024-11-15 19:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reports', '0002_auto_20241115_1327'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='report',
            unique_together={('owner', 'reported_post')},
        ),
    ]
