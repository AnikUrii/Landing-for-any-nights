# Generated by Django 3.0 on 2022-02-16 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0006_descriptionour_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descriptionour',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='In work?'),
        ),
    ]