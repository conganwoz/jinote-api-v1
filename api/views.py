from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .utils import request_utils
from .actions import note_actions
import json

def say_hello(reuqest):
    return HttpResponse('Hello World')

def upload_note(request):
    body = request_utils.decode_body(request)

    params = note_actions.process_upload_params(body)

    validate_result = note_actions.validate_params_upload(params)

    if validate_result['is_valid']:
        saved_note = note_actions.insert(validate_result.get('params'))
        return JsonResponse({
            'success': True,
            'note': note_actions.format(saved_note),
            'message': 'Lưu ghi chú thành công'
        })
    else:
        return JsonResponse(validate_result)

