from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from grade_app.models import Grade
from grade_app.serializers import Grade_Serializer
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from student_app.models import Student
from subject_app.models import Subject

# Create your views here.


class All_Grades(APIView):
    def post(self, request):
        subject_data = request.data['a_subject']
        # subject_instance = Subject.objects.get(id=subject_data)
        student_data = request.data['student']
        # student_instance = Student.objects.get(id=student_data)
        new_grade = {
            "grade": 100.00, "a_subject": subject_data, "student": student_data}
        ser_grade = Grade_Serializer(data=new_grade)
        if ser_grade.is_valid():
            ser_grade.save()
            return Response(ser_grade.data, status=HTTP_201_CREATED)
        else:
            print(ser_grade.errors)
            return Response(ser_grade.errors, status=HTTP_400_BAD_REQUEST)


class A_Grade(APIView):
    def put(self, request, id):
        grade = Grade.objects.get(id=id)
        if 'grade' in request.data and request.data['grade']:
            grade.grade = request.data.get('grade')
        ser_grade = Grade_Serializer(grade, data=vars(grade))
        if ser_grade.is_valid():
            ser_grade.save()
            return Response(ser_grade.data, status=HTTP_204_NO_CONTENT)
        else:
            print(ser_grade.errors)
            return Response(ser_grade.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        grade = Grade.objects.get(id=id)
        grade.delete()
        return Response(status=HTTP_204_NO_CONTENT)
