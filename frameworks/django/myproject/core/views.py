from django.shortcuts import render
from django.http import HttpResponse
''' This module is a request handler '''
# Create your views here.
# Request => Response


def hello(request):
    return HttpResponse("Hello from django")