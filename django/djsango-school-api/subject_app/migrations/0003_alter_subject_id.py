# Generated by Django 5.0.3 on 2024-03-22 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject_app', '0002_alter_subject_professor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
