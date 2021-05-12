from io import BytesIO
from os import path

from flask_testing import TestCase

from project import create_app

app = create_app()


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app

    def setUp(self):
        path_img_sent = path.join(self.app.config['ASSETS_DEFAULT_DIR'], 'valentin.jpg')
        with open(path_img_sent, 'rb') as img:
            self.img_sent_bytes = BytesIO(img.read())

    def tearDown(self):
        pass
