# Generated by Django 2.2.12 on 2021-03-07 02:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trelloApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lists',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 7, 2, 58, 18, 153020, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 7, 2, 58, 18, 167694, tzinfo=utc)),
        ),
    ]