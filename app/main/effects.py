from io import StringIO, BytesIO

from PIL import Image
from flask import Blueprint, jsonify, send_file

effects_blueprint = Blueprint('effects', __name__, url_prefix='/api/v1/effects')


@effects_blueprint.route('/default', methods=['GET'])
def get_default():
    img = Image.open('C:\\Users\\Valentin\\Pictures\\neural-transfer\\original\\aeri.jpg')
    # img = Image.new('RGB', ...)
    return serve_pil_image(img)


@effects_blueprint.route('/default', methods=['POST'])
def post_default():
    img = Image.open('C:\\Users\\Valentin\\Pictures\\neural-transfer\\original\\aeri.jpg')
    # img = Image.new('RGB', ...)
    return serve_pil_image(img)


def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=100)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')