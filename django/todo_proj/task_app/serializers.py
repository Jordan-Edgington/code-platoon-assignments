from rest_framework import serializers
from task_app.models import Task
from subtask_app.serializers import Subtask_Serializer


class Task_Serializer(serializers.ModelSerializer):
    subtasks = Subtask_Serializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'task_name', 'completed', 'subtasks']
