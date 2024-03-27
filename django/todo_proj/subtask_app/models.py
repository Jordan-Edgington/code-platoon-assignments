from django.db import models
from task_app.models import Task
# Create your models here.


class Subtask(models.Model):
    subtask_name = models.CharField()
    completed = models.BooleanField(default=True)
    parent_task = models.ForeignKey(
        Task, on_delete=models.CASCADE, blank=True)
# SUBTASK

# id - bigint
# sub_task_name - char
# completed - boolean
# parent_task - foreign key to task - id
