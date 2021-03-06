# Generated by Django 3.2 on 2021-04-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_remove_todo_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]
