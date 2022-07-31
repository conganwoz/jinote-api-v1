from django.shortcuts import render
from django.http import HttpResponse

def say_hello(reuqest):
    return HttpResponse('Hello World')

