# Generated by Django 5.0.3 on 2024-03-27 21:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('list_app', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField()),
                ('completed', models.BooleanField(default=False)),
                ('parent_list', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='list_app.list')),
            ],
        ),
    ]
