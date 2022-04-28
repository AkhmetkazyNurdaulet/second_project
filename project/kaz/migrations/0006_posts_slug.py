# Generated by Django 4.0.2 on 2022-04-07 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaz', '0005_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='slug',
            field=models.SlugField(default=True, max_length=255, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
    ]