# Generated by Django 3.2.13 on 2022-05-13 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 5, 13, 18, 24, 24, 460293)),
        ),
    ]
