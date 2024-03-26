from django.shortcuts import render, get_object_or_404
from .serializers import StudentAllSerializer2, Student, StudentAllSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from subject_app.models import Subject
# Create your views here.


class All_Students(APIView):
    def get(self, request):
        students = StudentAllSerializer2(Student.objects.all(), many=True)
        return Response(students.data)

    def post(self, request):
        new_student = StudentAllSerializer(data=request.data)
        if new_student.is_valid():
            new_student.save()
            return Response(new_student.data, status=HTTP_201_CREATED)
        else:
            return Response(new_student.errors, status=HTTP_400_BAD_REQUEST)


class A_Student(APIView):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        return Response(StudentAllSerializer2(student).data)

    def put(self, request, id):
        student = get_object_or_404(Student, id=id)
        ser_student = StudentAllSerializer2(
            student, data=request.data, partial=True)
        if ser_student.is_valid():
            ser_student.save()
            return Response(status=HTTP_204_NO_CONTENT)
        else:
            print(ser_student.errors)
            return Response(ser_student.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = get_object_or_404(Student, id=id)
        student.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Add_Subject_To_Student(APIView):
    def put(self, request, id, subject_id):
        student = get_object_or_404(Student, id=id)
        if not Subject.objects.filter(id=subject_id):
            return Response({"ERROR": "Subject ID does not exist."}, status=HTTP_400_BAD_REQUEST)
        student.add_subject(subject_id)
        student.save()
        return Response(status=HTTP_204_NO_CONTENT)
