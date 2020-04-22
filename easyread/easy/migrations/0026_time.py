# Generated by Django 3.0.5 on 2020-04-22 07:03

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easy', '0025_delete_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_input', models.CharField(max_length=15)),
                ('time_output', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=2)),
            ],
            options={
                'unique_together': {('time_input',)},
            },
        ),
    ]