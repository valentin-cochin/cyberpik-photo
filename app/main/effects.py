from io import BytesIO
from os import path

from PIL import Image
from flask import Blueprint, send_file

from app.config import BaseConfig

effects_blueprint = Blueprint('effects', __name__, url_prefix='/api/v1/effects')


@effects_blueprint.route('/default', methods=['GET'])
def get_default():
    file_path = path.join(BaseConfig.ASSETS_DEFAULT_DIR, "valentin.jpg")
    img = Image.open(file_path)
    return serve_pil_image(img)


@effects_blueprint.route('/default', methods=['POST'])
def post_default():
    img = Image.open('C:\\Users\\Valentin\\Pictures\\neural-transfer\\original\\aeri.jpg')
    return serve_pil_image(img)


def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=100)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')