from rest_framework import serializers
from subtask_app.models import Subtask


class Subtask_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['id', 'subtask_name', 'completed']
