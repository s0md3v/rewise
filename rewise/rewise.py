import json
import re

from urllib import parse, request


def _request(url, data):
    """This function is responsible for making HTTP GET requests.

    Args:
        url (str): url
        data (dict): query data

    Returns:
        str : HTTP body
    """
    query_str = parse.urlencode(data)
    url += '?' + query_str
    response = request.urlopen(url)
    body = response.read().decode(response.headers.get_content_charset())
    response.close()
    return body


def _query(q, lang='en-US'):
    """This function returns the HTTP body returned by Google.

    Args:
        q (str): query string
        lang (str): language in ISO 639 format

    Returns:
        str : HTTP body
    """
    api_url = 'http://www.google.com/complete/search'
    payload = {
        'q': q,
        'client': 'gws-wiz',
        'xssi': 't',
        'hl': lang,
    }
    return _request(api_url, payload)


def _load(body):
    """This function cleans Google's response and coverts
    it to JSON.

    Args:
        body (str): HTTP body

    Returns:
        dict
    """
    clean = re.search(r'\[.*\]', body).group(0)
    return json.loads(clean)


def _parse(body, mode='revise'):
    """This function parses the data returned by Google according
    to the specified mode.

    Args:
        body (str): HTTP body
        mode (str): parsing mode

    Returns:
        dict : when mode is 'raw' or 'revise'
        str  : when mode is 'correct'
        list : when mode is 'complete'
    """
    data = _load(body)
    suggestions = data[0] if data and len(data) > 0 else []
    correction_data = data[1] if data and len(data) > 1 else {}
    if mode == 'correct':
        return re.sub(r'</?sc>', '', correction_data.get('o', ''))
    elif mode == 'complete':
        return [re.sub(r'</?b>', '', item[0]) for item in suggestions]
    else:
        parsed = {
            'corrected': '',
            'completed': [],
        }
        parsed['corrected'] = re.sub(r'</?sc>', '', correction_data.get('o', ''))
        for item in suggestions:
            this = {
                'str': '',
                'fmt': '',
                'img': '',
                'info': '',
            }
            this['str'] = re.sub(r'</?b>', '', item[0])
            if len(item) > 3 and isinstance(item[3], dict):
                meta = item[3]
                this['fmt'] = meta.get('zh', '')
                this['img'] = meta.get('zs', '')
                this['info'] = meta.get('zi', '')
            parsed['completed'].append(this)
        return parsed


def raw(q, lang='en-US'):
    """This function returns the JSON data returned by Google.

    Args:
        q (str): query string
        lang (str): language in ISO 639 format

    Returns:
        dict
    """
    data = _load(_query(q, lang))
    return data


def revise(q, lang='en-US'):
    """This function returns a parsed version of Google's response
    only containing the fields that the author of this library
    considers useful.

    Args:
        q (str): query string
        lang (str): language in ISO 639 format

    Returns:
        dict
    """
    data = _query(q, lang)
    return _parse(data)


def correct(q, lang='en-US'):
    """This function returns the search query corrected by Google

    Args:
        q (str): query string
        lang (str): language in ISO 639 format

    Returns:
        str
    """
    data = _query(q, lang)
    return _parse(data, 'correct')


def complete(q, lang='en-US'):
    """This function returns auto-completed search queries suggested
    by Google.

    Args:
        q (str): query string
        lang (str): language in ISO 639 format

    Returns:
        list
    """
    data = _query(q, lang)
    return _parse(data, mode='complete')
