# Generated by Django 4.2.3 on 2023-07-15 18:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hackathon',
            name='end_date',
        ),
        migrations.AddField(
            model_name='hackathon',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 15, 18, 45, 7, 47677)),
        ),
        migrations.AddField(
            model_name='submission',
            name='user_id',
            field=models.IntegerField(default=datetime.datetime(2023, 7, 15, 18, 45, 31, 319398)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hackathon',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 15, 18, 45, 7, 47668)),
        ),
    ]