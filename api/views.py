from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .utils import request_utils
from .actions import note_actions
import json

def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    return render(request, 'chat/room.html', {'room_name': room_name})


def say_hello(reuqest):
    return HttpResponse('Hello World')


def upload_note(request):
    body = request_utils.decode_body(request)
    params = note_actions.parse_upload_params(body)
    validation_result = note_actions.validate_upload_params(params)

    if validation_result['is_valid']:
        saved_note = note_actions.insert(validation_result.get('params'))

        return JsonResponse({
            'success': True,
            'note': note_actions.format(saved_note),
            'message': 'Lưu ghi chú thành công. '\
                       'Hãy lưu trữ mã mở khoá của bạn để dùng lại.'
        })
    else:
        return JsonResponse(validation_result)

def publish_notes(request):
    body = request_utils.decode_body(request)
    params = note_actions.parse_publish_params(body)

    note_actions.do_publish_notes(params)

    return JsonResponse({'success': True, 'message': 'Đã xuất bản ghi chú thành công'})


def get_publish_notes(request):
    body = request_utils.decode_body(request)
    params = note_actions.parse_get_publish_notes_params(body)

    data = note_actions.do_get_publish_notes(params)

    return JsonResponse({'success': True, data: data})


def download_notes(request):
    body = request_utils.decode_body(request)
    params = note_actions.parse_download_params(body)
    notes = note_actions.get_notes_by_password(params)

    return JsonResponse({'success': True, 'notes': notes})


