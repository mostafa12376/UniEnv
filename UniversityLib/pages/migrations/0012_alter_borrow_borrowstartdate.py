# Generated by Django 3.2.5 on 2021-07-16 20:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_alter_borrow_borrowstartdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='borrowStartDate',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 20, 25, 5, 865335, tzinfo=utc)),
        ),
    ]