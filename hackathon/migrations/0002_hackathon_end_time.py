# Generated by Django 4.2.3 on 2023-07-16 07:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathon',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 16, 7, 29, 59, 423487, tzinfo=datetime.timezone.utc)),
        ),
    ]
