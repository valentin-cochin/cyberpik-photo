import imghdr
from io import BytesIO
from os import path

from PIL import Image
from flask import Blueprint, current_app, request, send_file
from werkzeug.utils import secure_filename

from project.api.img_modifier.NeuralTransferStyle import NeuralTransferStyle

effects_blueprint = Blueprint('effects', __name__, url_prefix='/api/v1/effects')


@effects_blueprint.route('/default', methods=['GET'])
def get_default():
    file_path = path.join(current_app.config['ASSETS_DEFAULT_DIR'], "valentin.jpg")
    img = Image.open(file_path)
    return serve_pil_image(img)


@effects_blueprint.route('/default', methods=['POST'])
def post_default():
    uploaded_file = request.files['file']

    if allowed_image(uploaded_file):
        pil_image = Image.open(uploaded_file)
        return serve_pil_image(pil_image)
    else:
        return "Invalid image or filename", 422


@effects_blueprint.route('/', methods=['POST'])
def post_for_transformation():
    uploaded_file = request.files['file']

    if allowed_image(uploaded_file):
        original_img = Image.open(uploaded_file)
        nst = NeuralTransferStyle(current_app.config['NST_MODEL_DIR'], original_img)
        style_path = path.join(current_app.config['ASSETS_STYLE_DIR'], 'vaporwave-fluid.jpg')
        new_img = nst.stylize_image(style_path=style_path)
        return serve_pil_image(new_img)
    else:
        return "Invalid image or filename", 422


def allowed_image(file):
    filename = secure_filename(file.filename)

    if filename == '':
        return False
    else:
        file_ext = path.splitext(filename)[1]
        file_ext = file_ext.lower()
        is_file_ext_allowed = file_ext in current_app.config['ALLOWED_IMAGE_EXTENSIONS']
        is_image_validated = (file_ext == validate_image(file.stream))
        return is_file_ext_allowed and is_image_validated


def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=100)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')
