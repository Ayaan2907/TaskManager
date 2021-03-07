# Generated by Django 2.2.12 on 2021-03-07 07:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trelloApp', '0007_auto_20210307_0702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('time_stamp', models.DateTimeField(default=datetime.datetime(2021, 3, 7, 7, 4, 50, 821651, tzinfo=utc))),
                ('note', models.TextField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 7, 7, 4, 50, 836132, tzinfo=utc)),
        ),
    ]
