from django.shortcuts import render, get_object_or_404
from .serializers import SubjectSerializer, Subject
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
# Create your views here.


class All_Subjects(APIView):
    def get(self, request):
        subjects = SubjectSerializer(Subject.objects.all(), many=True)
        return Response(subjects.data)

    def post(self, request):
        new_subject = SubjectSerializer(data=request.data)
        if new_subject.is_valid():
            new_subject.save()
            return Response(new_subject.data, status=HTTP_201_CREATED)
        else:
            return Response(new_subject.errors, status=HTTP_400_BAD_REQUEST)


class A_Subject(APIView):
    def get(self, request, subject):
        a_subject = get_object_or_404(Subject, subject_name=subject.title())
        return Response(SubjectSerializer(a_subject).data)

    def put(self, request, subject):
        subject = Subject.objects.get(subject_name=subject)
        ser_subject = SubjectSerializer(
            subject, data=request.data, partial=True)
        if ser_subject.is_valid():
            ser_subject.save()
            return Response(status=HTTP_204_NO_CONTENT)
        else:
            print(ser_subject.errors)
            return Response(ser_subject.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, subject):
        subject = get_object_or_404(Subject, subject_name=subject)
        subject.delete()
        return Response(status=HTTP_204_NO_CONTENT)
