# Generated by Django 4.0.5 on 2022-07-25 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0006_remove_task_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
