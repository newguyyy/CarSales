from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view()
def say_hello(request):
    # return render(request,'hello.html',{'name':'TOV'})
    return Response('Hello World')
    # return HttpResponse('Hello World')