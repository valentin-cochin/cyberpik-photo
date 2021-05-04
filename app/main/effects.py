from flask import Blueprint, jsonify

effects_blueprint = Blueprint('effects', __name__, url_prefix='/api/v1/effects')


@effects_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
