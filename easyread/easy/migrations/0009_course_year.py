# Generated by Django 3.0.5 on 2020-04-21 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easy', '0008_remove_course_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='year',
            field=models.CharField(choices=[('year1', 'YEAR 1'), ('year2', 'YEAR 2'), ('year3', 'YEAR 3'), ('year4', 'YEAR 4')], default='Year1', max_length=20),
        ),
    ]
