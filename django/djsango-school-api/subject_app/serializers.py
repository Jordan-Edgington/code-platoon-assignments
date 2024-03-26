from rest_framework import serializers
from subject_app.models import Subject
from grade_app.models import Grade


class SubjectSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()
    grade_average = serializers.SerializerMethodField()
    # grades = Grade_Serializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = ['subject_name', 'professor', 'students', 'grade_average']

    def get_students(self, obj):
        students = obj.students.all()
        students_response = len([student.name for student in students])
        return students_response

    def get_grade_average(self, obj):
        # obj is the Subject instance being serialized
        grades = Grade.objects.filter(a_subject=obj)
        if grades.exists():
            total_grades = sum(grade.grade for grade in grades)
            average_grade = total_grades / len(grades)
            rounded_avg = round(average_grade, 2)
            return rounded_avg
        else:
            return None
