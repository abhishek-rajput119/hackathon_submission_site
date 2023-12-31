# Generated by Django 4.2.3 on 2023-07-16 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0010_delete_submission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hackathon_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('summary', models.TextField()),
                ('title', models.CharField(max_length=100, null=True)),
                ('link', models.TextField()),
                ('file', models.TextField()),
            ],
        ),
    ]
