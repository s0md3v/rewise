import json
import re

from urllib import parse, request


def _request(url, data):
    query_str = parse.urlencode(data)
    url += '?' + query_str
    response = request.urlopen(url)
    body = response.read().decode(response.headers.get_content_charset())
    response.close()
    return body


def _query(q, lang='en-US'):
    api_url = 'https://www.google.com/complete/search'
    payload = {
        'q': q,
        'cp': 1,
        'client': 'psy-ab',
        'xssi': 't',
        'gs_ri': 'gws-wiz',
        'hl': lang,
    }
    return _request(api_url, payload)


def _load(body):
    clean = re.sub(r'^[^\[]*\n\[', '[', body)
    return json.loads(clean)


def _parse(body, mode='revise'):
    data = _load(body)
    complete, correct = data[0], data[1]
    if mode == 'correct':
        return re.sub(r'</?sc>', '', correct.get('o', ''))
    elif mode == 'complete':
        return [re.sub(r'</?b>', '', item[0]) for item in complete]
    else:
        parsed = {
            'corrected': '',
            'completed': [],
        }
        parsed['corrected'] = re.sub(r'</?sc>', '', correct.get('o', ''))
        for item in complete:
            this = {
                'str': '',
                'fmt': '',
                'img': '',
                'info': '',
            }
            this['str'] = re.sub(r'</?b>', '', item[0])
            if len(item) > 3:
                meta = item[3]
                this['fmt'] = meta.get('zh', '')
                this['img'] = meta.get('zs', '')
                this['info'] = meta.get('zi', '')
            parsed['completed'].append(this)
        return parsed


def raw(q, lang='en-US'):
    data = _load(_query(q, lang))
    return data


def revise(q, lang='en-US'):
    data = _query(q, lang)
    return _parse(data)


def correct(q, lang='en-US'):
    data = _query(q, lang)
    return _parse(data, 'correct')


def complete(q, lang='en-US'):
    data = _query(q, lang)
    return _parse(data, mode='complete')
