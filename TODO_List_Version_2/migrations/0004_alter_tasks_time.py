# Generated by Django 4.2.14 on 2024-09-25 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODO_List_Version_2', '0003_alter_tasks_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='Time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
