# Generated by Django 3.2.8 on 2021-11-27 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0020_auto_20211127_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
    ]
