# Generated by Django 5.0.6 on 2024-06-19 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_task_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='category_id',
            new_name='category',
        ),
    ]
