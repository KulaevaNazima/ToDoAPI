# Generated by Django 3.2 on 2021-04-12 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_auto_20210412_1923'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='Task',
        ),
    ]
