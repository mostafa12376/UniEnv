# Generated by Django 3.2.5 on 2021-07-15 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=300, null=True)),
                ('ISBN', models.CharField(max_length=13, unique=True)),
                ('pubYear', models.IntegerField(blank=True, null=True)),
                ('category', models.CharField(choices=[('Fantasy', 'Fantasy'), ('Sci-fi', 'Sci-fi'), ('Mystery', 'Mystery'), ('Programming Language', 'Programming Language'), ('Autobiography', 'Autobiography'), ('Historical', 'Historical'), ('Technologies', 'Technologies'), ('Guide / How-to', 'Guide / How-to'), ('Families & Relationships', 'Families & Relationships')], default=('Fantasy', 'Fantasy'), max_length=24)),
                ('copies', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowStartDate', models.DateField(auto_now=True)),
                ('borrowPeriod', models.IntegerField(default=7)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.account')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.book')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='borrowedBooks',
            field=models.ManyToManyField(through='pages.Borrow', to='pages.Book'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
