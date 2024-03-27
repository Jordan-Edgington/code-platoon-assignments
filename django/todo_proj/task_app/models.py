from django.db import models
from list_app.models import List
# Create your models here.


class Task(models.Model):
    task_name = models.CharField()
    completed = models.BooleanField(default=False)
    parent_list = models.ForeignKey(
        List, on_delete=models.CASCADE, blank=True)

# TASK

# id
# task_name - char
# completed - boolean
# parent_list - foreign key to list - list_name
