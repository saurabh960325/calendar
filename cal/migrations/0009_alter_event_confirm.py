# Generated by Django 3.2.4 on 2021-06-14 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0008_auto_20210614_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='confirm',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
