# Generated by Django 3.0.5 on 2020-04-21 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easy', '0012_auto_20200421_0355'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('course_code', 'course_name')},
        ),
    ]
