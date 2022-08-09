from ..utils import common
from api.models import Note

def process_upload_params(body):
    title = body.get('title')
    content = body.get('content')
    alias = body.get('alias')
    password = body.get('password')

    default_params = {
        'title': '',
        'content': '',
        'alias': '',
        'hashed_unlock_key': '$2b$12$PYG.ObLDW90BlCnAawSZHOxybm5iMxCjRFBKokVK0VvPXwvUj3hf6',
        'password': password
    }

    if not common.is_empty(title):
        default_params['title'] = title

    if not common.is_empty(content):
        default_params['content'] = content

    if not common.is_empty(alias):
        default_params['alias'] = alias

    # TODO add hash password

    return default_params

def validate_params_upload(params):
    if common.is_empty(params):
        return {
            'is_valid': False,
            'message': 'Dữ liệu không hợp lệ',
            'params': None
        }

    if common.is_empty(params.get('content')):
        return {
            'is_valid': False,
            'message': 'Vui lòng nhập nội dung của note',
            'params': None
        }

    if common.is_empty(params.get('password')):
        return {
            'message': 'Vui lòng nhập password mở khoá bài viết',
            'is_valid': False,
            'params': None
        }

    if common.is_empty(params.get('hashed_unlock_key')):
        return {
            'is_valid': False,
            'message': 'Lỗi xử lý dữ liệu. Vui lòng thử lại sau',
            'params': None
        }

    return {
        'is_valid': True,
        'message': None,
        'params': params
    }

def insert(params):
    title = params['title']
    content = params['content']
    alias = params['alias']
    hashed_unlock_key = params['hashed_unlock_key']

    note = Note(title=title, content=content, alias=alias, hashed_unlock_key=hashed_unlock_key)
    note.save()

    return note


def format(note):
    title = note.title or ''
    content = note.content or ''
    alias = note.alias or ''
    inserted_at = note.inserted_at
    updated_at = note.updated_at

    inserted_at = common.convert_to_vn_time(inserted_at)
    inserted_at = common.format_datetime(inserted_at)

    updated_at = common.convert_to_vn_time(updated_at)
    updated_at = common.format_datetime(updated_at)

    return {
        'title': title,
        'content': content,
        'alias': alias,
        'inserted_at': inserted_at,
        'updated_at': updated_at
    }

