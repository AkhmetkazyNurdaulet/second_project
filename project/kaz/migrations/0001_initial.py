# Generated by Django 4.0.2 on 2022-03-22 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_name', models.CharField(max_length=5000)),
                ('tour_inf', models.CharField(max_length=5000)),
                ('tour_id', models.IntegerField()),
            ],
        ),
    ]
