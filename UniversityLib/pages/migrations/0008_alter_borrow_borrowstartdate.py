# Generated by Django 3.2.5 on 2021-07-16 18:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_borrow_borrowstartdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='borrowStartDate',
            field=models.DateField(default=datetime.date),
        ),
    ]
