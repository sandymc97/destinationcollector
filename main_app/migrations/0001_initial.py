# Generated by Django 4.2.3 on 2023-07-26 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('continent', models.CharField(max_length=100)),
                ('climate', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
            ],
        ),
    ]
