# Generated by Django 5.0.4 on 2024-04-27 15:47

import django.template.defaulttags
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='start_date',
            field=models.DateField(default=django.template.defaulttags.now),
        ),
    ]
