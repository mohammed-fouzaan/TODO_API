# Generated by Django 4.2.6 on 2023-10-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_tasks_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='created',
            field=models.CharField(default='on 28/10/2023 at 17:35:37', editable=False, max_length=200),
        ),
    ]
