from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Car
from .serializers import car_serializer

# Create your views here.

@api_view()
def car_list(request):
    return Response("ok")
    # cars = Car.objects.all()
    # serializer = car_serializer(cars,many=True)
    # return Response(serializer.data)