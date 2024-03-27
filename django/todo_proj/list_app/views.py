from django.shortcuts import render, get_object_or_404, get_list_or_404
from .serializers import List_Serializer, List
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK

# Create your views here.


class All_Lists(APIView):
    def get(self, request):
        lists = List_Serializer(List.objects.all(), many=True)
        print(lists)
        for x in lists.data:
            print(x)
            print(x.get('list_name'))
        return Response(lists.data, status=HTTP_200_OK)

    def post(self, request):
        new_list = List_Serializer(data=request.data)
        if new_list.is_valid():
            new_list.save()
            return Response(new_list.data, status=HTTP_201_CREATED)
        else:
            return Response(new_list.errors, status=HTTP_400_BAD_REQUEST)


class A_List(APIView):
    def get(self, request, list_id):
        list = get_object_or_404(List, id=list_id)
        return Response(List_Serializer(list).data, status=HTTP_200_OK)

    def put(self, request, list_id):
        list = get_object_or_404(List, id=list_id)
        ser_list = List_Serializer(list, data=request.data, partial=True)
        if ser_list.is_valid():
            ser_list.save()
            return Response(status=HTTP_204_NO_CONTENT)
        else:
            print(ser_list.errors)
            return Response(ser_list.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, list_id):
        list = get_object_or_404(list, id=list_id)
        list.delete()
        return Response(status=HTTP_204_NO_CONTENT)
