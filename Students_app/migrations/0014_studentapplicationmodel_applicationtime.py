# Generated by Django 3.2.11 on 2022-01-17 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students_app', '0013_applicationtypemodel_studentapplicationmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentapplicationmodel',
            name='applicationTime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]