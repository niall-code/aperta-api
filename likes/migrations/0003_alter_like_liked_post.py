# Generated by Django 3.2.23 on 2024-11-13 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_id'),
        ('likes', '0002_auto_20241102_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='liked_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='posts.post'),
        ),
    ]
