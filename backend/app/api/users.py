from flask import jsonify, current_app, abort

from flask_login import current_user

from app.exceptions import BadRequest

from app.models import User
from app.api import api


@api.route('/users', methods=['GET'])
def _get_users():
    try:
        users = User.query.all()
        return jsonify(list(map(lambda s: s.to_json(), users)))
    except Exception as e:
        current_app.logger.error(e)
        abort(500, description='Server error')


@api.route('/users/<int:id>', methods=['GET'])
def _get_user(id: int):
    try:
        user = User.query.filter_by(id=id).first()
        if not user:
            raise BadRequest('user not found')

        return jsonify(user.to_json())
    except BadRequest as e:
        abort(400, description=str(e))
    except Exception as e:
        current_app.logger.error(e)
        abort(500, description='Server error')


@api.route('/users/current', methods=['GET'])
def _get_current_user():
    try:
        return jsonify(current_user.to_json())
    except Exception as e:
        current_app.logger.error(e)
        abort(500, description='Server error')
