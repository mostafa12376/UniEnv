# Generated by Django 3.2.5 on 2021-07-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_account_borrowedbooks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='borrowedBooks',
            field=models.ManyToManyField(through='pages.Borrow', to='pages.Book'),
        ),
    ]
