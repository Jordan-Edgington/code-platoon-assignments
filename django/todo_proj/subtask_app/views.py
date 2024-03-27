from django.shortcuts import render, get_object_or_404, get_list_or_404
from .serializers import Subtask_Serializer, Subtask
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK

# Create your views here.


class All_Subtasks(APIView):
    def get(self, request, list_id, task_id):
        subtasks = Subtask_Serializer(Subtask.objects.all(), many=True)
        return Response(subtasks.data, status=HTTP_200_OK)

    def post(self, request, list_id, task_id):
        new_subtask = request.data
        new_subtask["parent_task"] = task_id
        ser_subtask = Subtask_Serializer(data=new_subtask)
        if ser_subtask.is_valid():
            ser_subtask.save()
            return Response(ser_subtask.data, status=HTTP_201_CREATED)
        else:
            return Response(ser_subtask.errors, status=HTTP_400_BAD_REQUEST)


class A_Subtask(APIView):
    def get(self, request, list_id, task_id, subtask_id):
        subtask = get_object_or_404(Subtask, id=subtask_id)
        return Response(Subtask_Serializer(subtask).data, status=HTTP_200_OK)

    def put(self, request, list_id, task_id, subtask_id):
        subtask = get_object_or_404(Subtask, id=subtask_id)
        ser_subtask = Subtask_Serializer(
            subtask, data=request.data, partial=True)
        if ser_subtask.is_valid():
            ser_subtask.save()
            return Response(status=HTTP_204_NO_CONTENT)
        else:
            print(ser_subtask.errors)
            return Response(ser_subtask.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, list_id, task_id, subtask_id):
        subtask = get_object_or_404(Subtask, id=subtask_id)
        subtask.delete()
        return Response(status=HTTP_204_NO_CONTENT)
