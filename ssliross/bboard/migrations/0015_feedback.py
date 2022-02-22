# Generated by Django 3.0 on 2022-02-17 19:00

import bboard.utilities
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0014_button'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('avatar', models.ImageField(blank=True, upload_to=bboard.utilities.get_timestamp_path, verbose_name='Avatar')),
                ('description', models.TextField(verbose_name='Desc')),
            ],
            options={
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Feedbacks',
            },
        ),
    ]