# Generated by Django 3.0.5 on 2020-04-21 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easy', '0021_remove_document_output_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='output_file',
            field=models.FileField(default='output', upload_to=''),
        ),
    ]
