# Generated by Django 2.2.12 on 2021-03-11 04:53

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List_board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Task_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 3, 11, 4, 53, 55, 719937, tzinfo=utc))),
                ('board_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workingApp.List_board')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 3, 11, 4, 53, 55, 720324, tzinfo=utc))),
                ('due_date', models.DateTimeField()),
                ('list_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workingApp.Task_list')),
            ],
        ),
    ]
