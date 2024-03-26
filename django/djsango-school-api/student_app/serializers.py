from rest_framework import serializers
from .models import Student
from subject_app.serializers import SubjectSerializer


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'student_email', 'locker_number']


class StudentAllSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['name', 'student_email', 'personal_email',
                  'locker_number', 'locker_combination', 'good_student', 'subjects']

    def get_subjects(self, obj):
        subjects = obj.subjects.all()
        subjects_response = [x.subject_name for x in subjects]
        return subjects_response


class StudentAllSerializer2(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = Student
        fields = ['name', 'student_email', 'personal_email',
                  'locker_number', 'locker_combination', 'good_student', 'subjects']
