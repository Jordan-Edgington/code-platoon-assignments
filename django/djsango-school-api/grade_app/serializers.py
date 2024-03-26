from rest_framework import serializers
from grade_app.models import Grade


class Grade_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'
