# Generated by Django 3.2.8 on 2021-11-27 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_forum_enabled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='Ins',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='TAs',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='studs',
        ),
        migrations.AddField(
            model_name='forum',
            name='name',
            field=models.CharField(default='FORUM', max_length=20),
        ),
    ]
