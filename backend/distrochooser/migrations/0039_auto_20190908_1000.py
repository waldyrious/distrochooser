# Generated by Django 2.2.5 on 2019-09-08 10:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distrochooser', '0038_auto_20190908_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersession',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 8, 10, 0, 41, 104673)),
        ),
    ]