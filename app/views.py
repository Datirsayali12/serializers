from django.http import HttpResponse
from django.shortcuts import render
from django.core.signals import  request_finished
from django.dispatch import receiver
from .models import *

# Create your views here.


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItemSerializer
from .models import Item

@api_view(['POST'])
def create_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        # Manually create the Item instance using validated data
        item = Item.objects.create(
            name=serializer.validated_data['name'],
            price=serializer.validated_data['price'],
            quantity=serializer.validated_data['quantity']
        )
        return Response({"message": "Item created successfully!", "data": serializer.validated_data})
    else:
        # Return errors if validation fails
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# def trigger_500_error(request):
#     return HttpResponseServerError("Simulated server error")
#
# def trigger_403_error(request):
#     raise PermissionDenied
#
# def trigger_400_error(request):
#     raise BadRequest
#
#
# @receiver(request_finished)
# def func(sender,**kwargs):
#     print("finished request")
#
