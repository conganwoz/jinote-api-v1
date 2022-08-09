from django.shortcuts import render
from django.http import HttpResponse

import json

def say_hello(reuqest):
    return HttpResponse('Hello World')

def upload_note(request):
    print('in_here_')
    print(request)
    body = request.body.decode('utf-8')
    body = json.loads(body)
    content = body['content']
    print(content)
    return HttpResponse("ok")

