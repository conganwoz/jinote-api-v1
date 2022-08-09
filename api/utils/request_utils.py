import json

def decode_body(request):
    body = request.body.decode('utf-8')
    body = json.loads(body)

    return body

