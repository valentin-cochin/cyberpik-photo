from flask import Blueprint, jsonify

effects_blueprint = Blueprint('effects', __name__)


@effects_blueprint.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
