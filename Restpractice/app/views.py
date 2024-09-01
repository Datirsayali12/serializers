from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET', 'POST'])
def student_list_create(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def user_list(request,pk):
    data=request.get
    print(data)
    students = Student.objects.get(pk=pk)
    serializer = StudentSerializer(students)
    return Response(serializer.data)

@api_view(['POST', 'PUT'])
def data_save(request, pk=None):
    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data saved successfully"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Error while saving data", "errors": serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT" and pk is not None:
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({"message": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data updated successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Error while updating data", "errors": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_books(request):
    books=Book.objects.all()
    serializer=BookSerializer(books,many=True)
    return Response({"data":serializer.data})


@api_view(['GET','POST','PUT','DELETE'])
def get_book(request,pk):
    if request.method=="GET":
        books = Book.objects.get(pk=pk)
        serializer = BookSerializer(books)
        return Response({"data": serializer.data})

    if request.method=='POST':
        data=request.data
        serializer=BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"data save"})
        else:
            return Response(serializer.errors)

    if request.method=="PUT":
        book=Book.objects.get(pk=pk)
        serializer=BookSerializer(data=book)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"data is updated"})
        else:
            return Response(serializer.errors)





