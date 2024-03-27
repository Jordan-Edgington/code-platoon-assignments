from django.shortcuts import render, get_object_or_404, get_list_or_404
from .serializers import Task_Serializer, Task
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK

# Create your views here.


class All_Tasks(APIView):
    def get(self, request, list_id):
        tasks = Task_Serializer(Task.objects.all(), many=True)
        return Response(tasks.data, status=HTTP_200_OK)

    def post(self, request, list_id):
        new_task = request.data
        new_task["parent_list"] = list_id
        ser_task = Task_Serializer(data=new_task)
        if ser_task.is_valid():
            ser_task.save()
            return Response(ser_task.data, status=HTTP_201_CREATED)
        else:
            return Response(ser_task.errors, status=HTTP_400_BAD_REQUEST)


class A_Task(APIView):
    def get(self, request, list_id, task_id):
        task = get_object_or_404(Task, id=task_id)
        return Response(Task_Serializer(task).data, status=HTTP_200_OK)

    def put(self, request, list_id, task_id):
        task = get_object_or_404(Task, id=task_id)
        ser_task = Task_Serializer(task, data=request.data, partial=True)
        if ser_task.is_valid():
            ser_task.save()
            return Response(status=HTTP_204_NO_CONTENT)
        else:
            print(ser_task.errors)
            return Response(ser_task.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, list_id, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return Response(status=HTTP_204_NO_CONTENT)
