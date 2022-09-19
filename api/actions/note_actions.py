from ..utils import common
from api.models import Note

def parse_upload_params(body):
    id = body.get('id')
    title = body.get('title')
    content = body.get('content')
    alias = body.get('alias')
    password = body.get('password')

    default_params = {
        'title': '',
        'content': '',
        'alias': '',
        'hashed_unlock_key': common.passlib_encryption(password),
        'password': password
    }

    if not common.is_empty(title):
        default_params['title'] = title

    if not common.is_empty(content):
        default_params['content'] = content

    if not common.is_empty(alias):
        default_params['alias'] = alias

    if not common.is_empty(id):
        default_params['id'] = id

    return default_params


def validate_upload_params(params):
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

    existed_note = None

    if not common.is_empty(params.get('id')):
        try:
            existed_note = Note.objects.get(id=params.get('id'))
        except Note.DoesNotExist:
            existed_note = None

        if common.is_empty(note):
            return {
                'is_valid': False,
                'message': 'Ghi chú không xác định',
                'params': None
            }

    if common.is_empty(params.get('password')):
        return {
            'message': 'Vui lòng nhập password mở khoá bài viết',
            'is_valid': False,
            'params': None
        }

    if (common.is_empty(params.get('hashed_unlock_key'))
            and common.is_empty(params.get('id'))):
        return {
            'is_valid': False,
            'message': 'Lỗi xử lý dữ liệu. Vui lòng thử lại sau',
            'params': None
        }

    return {
        'is_valid': True,
        'message': None,
        'params': params,
        'existed_note': existed_note
    }


def parse_download_params(body):
    alias = body.get('alias')
    password = body.get('password')

    return {
        'alias': alias or '',
        'password': password or ''
    }


def get_notes_by_password(params):
    alias = params['alias']
    password = params['password']
    password_hashed = common.passlib_encryption(password)

    notes = list(
        map(lambda note: format(note),
            Note.objects.filter(alias=alias)[::1])
    )
    notes = list(
        filter(
            lambda note:
                common.passlib_encryption_verify(
                    password, note.get('hashed_unlock_key')),
            notes
        )
    )

    return notes


def insert(params):
    title = params['title']
    content = params['content']
    alias = params['alias']
    hashed_unlock_key = params['hashed_unlock_key']

    note = Note(
        title=title,
        content=content,
        alias=alias,
        hashed_unlock_key=hashed_unlock_key
    )
    note.save()

    return note


def update(params):
    existed_note = params.get('existed_note')
    existed_note.title = params.get('title')
    existed_note.content = params.get('content')
    if not common.is_empty(params.get('alias')):
        existed_note.alias = params.get('alias')

    if not common.is_empty(params.get('hashed_unlock_key')):
        existed_note.hashed_unlock_key = params.get('hashed_unlock_key')

    existed_note.save()

    return existed_note


def format(note):
    id = note.id or ''
    title = note.title or ''
    content = note.content or ''
    alias = note.alias or ''
    inserted_at = note.inserted_at
    updated_at = note.updated_at
    hashed_unlock_key = note.hashed_unlock_key or ''

    inserted_at = common.convert_to_vn_time(inserted_at)
    inserted_at = common.format_datetime(inserted_at)

    updated_at = common.convert_to_vn_time(updated_at)
    updated_at = common.format_datetime(updated_at)

    return {
        'id': id,
        'title': title,
        'content': content,
        'alias': alias,
        'inserted_at': inserted_at,
        'updated_at': updated_at,
        'hashed_unlock_key': hashed_unlock_key
    }

