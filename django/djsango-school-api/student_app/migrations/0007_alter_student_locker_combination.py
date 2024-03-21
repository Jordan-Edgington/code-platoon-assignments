# Generated by Django 5.0.3 on 2024-03-20 20:18

import student_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0006_alter_student_locker_combination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='locker_combination',
            field=models.CharField(default='12-12-12', validators=[student_app.validators.validate_combination_format]),
        ),
    ]
