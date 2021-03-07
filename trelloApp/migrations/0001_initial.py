# Generated by Django 2.2.12 on 2021-03-07 02:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('time_stamp', models.DateTimeField(default=datetime.datetime(2021, 3, 7, 2, 56, 2, 293720, tzinfo=utc))),
                ('note', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('task_description', models.TextField(max_length=200)),
                ('time_stamp', models.DateTimeField(default=datetime.datetime(2021, 3, 7, 2, 56, 2, 309039, tzinfo=utc))),
                ('due_date', models.DateTimeField()),
            ],
        ),
    ]
