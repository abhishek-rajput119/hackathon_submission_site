# Generated by Django 4.2.3 on 2023-07-16 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0006_remove_submission_type_of_submission_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathon',
            name='background_image',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hackathon',
            name='hackathon_image',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='submission',
            name='file',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='submission',
            name='link',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='submission',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
