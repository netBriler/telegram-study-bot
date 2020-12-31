from flask import abort, Blueprint, json, jsonify

from flask_login import current_user

from app.models import User

api = Blueprint('api', __name__)


@api.route('/<path:path>')
def catch_all(path):
    abort(404, 'Not Found')


@api.errorhandler(Exception)
def handle_exception(e):
    return jsonify({
        'ok': False,
        'code': e.code,
        'description': e.description
    })


@api.after_request
def after_request(response):
    response_data = json.loads(response.get_data())

    if 'ok' not in response_data or response_data['ok']:
        data = dict()
        data['ok'] = True
        data['response'] = json.loads(response.get_data())
        response.set_data(json.dumps(data, sort_keys=False))
    return response


@api.before_request
def before_request():
    if not current_user.is_authenticated or not current_user.is_admin():
        abort(401)


from . import subjects
from . import users
