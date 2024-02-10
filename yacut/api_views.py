import re
from http import HTTPStatus

from flask import jsonify, request

from yacut import app, db
from yacut.error_handlers import InvalidAPiUsage
from yacut.models import URLMap
from yacut.views import get_unique_short_id

ID_NOT_FOUND = 'Указанный id не найден'
REQUEST_BODY_MISSING = 'Отсутствует тело запроса'
URL_MUST_HAVE = '\"url\" является обязательным полем!'
SHORT_NAME = 'Указано недопустимое имя для короткой ссылки'
NAME_TAKEN = 'Имя "py" уже занято.'

# Регулярное выражение для определения правильности имени для короткой ссылки
PATTERN_MATCH = r'^[a-zA-Z0-9]{1,16}$'


@app.route('/api/id/<string:custom_id>/', methods=('GET',))
def get_url(custom_id):
    url = URLMap.query.filter_by(short=custom_id).first()
    if url is not None:
        return jsonify(url=url.original), HTTPStatus.OK
    raise InvalidAPiUsage(ID_NOT_FOUND, HTTPStatus.NOT_FOUND)


@app.route('/api/id/', methods=('POST',))
def create_short_link():
    data = request.get_json()
    if not data:
        raise InvalidAPiUsage(REQUEST_BODY_MISSING, HTTPStatus.BAD_REQUEST)

    if 'url' not in data:
        raise InvalidAPiUsage(URL_MUST_HAVE, HTTPStatus.BAD_REQUEST)
    short_name = data.get('custom_id')

    if not short_name:
        data['custom_id'] = get_unique_short_id()

    if not re.match(PATTERN_MATCH, data['custom_id']):
        raise InvalidAPiUsage(SHORT_NAME.format(py=short_name),
                              HTTPStatus.BAD_REQUEST)

    if URLMap.query.filter_by(short=short_name).first():
        raise InvalidAPiUsage(NAME_TAKEN, HTTPStatus.BAD_REQUEST)
    url_map = URLMap()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED