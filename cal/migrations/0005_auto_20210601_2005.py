# Generated by Django 3.2.3 on 2021-06-01 14:35

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cal', '0004_auto_20210529_2025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='end_time',
            new_name='Meeting_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='event',
            name='Host_ID',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='Meeting_ClientID',
            field=models.EmailField(max_length=200),
        ),
    ]
