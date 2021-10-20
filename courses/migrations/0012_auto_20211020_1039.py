# Generated by Django 3.2.8 on 2021-10-20 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_filesubmission_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='maxmarks',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='filesubmission',
            name='grade',
            field=models.IntegerField(default=-1),
        ),
    ]
