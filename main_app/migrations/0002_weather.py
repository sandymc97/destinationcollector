# Generated by Django 4.2.3 on 2023-07-28 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('S', 'Sunny'), ('R', 'Rainy'), ('C', 'Cloudy')], default='S', max_length=1)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.destination')),
            ],
        ),
    ]