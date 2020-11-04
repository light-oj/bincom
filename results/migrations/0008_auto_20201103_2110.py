# Generated by Django 3.1.3 on 2020-11-03 20:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0007_auto_20201103_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcedlgaresults',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='announcedpuresults',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='announcedstateresults',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='announcedwardresults',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='lga',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='pollingunit',
            name='date_entered',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='ward',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]