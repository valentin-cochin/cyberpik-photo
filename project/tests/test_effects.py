import json
import unittest
from io import BytesIO
from os import path

import werkzeug
from PIL import Image

from project.tests.base import BaseTestCase


class TestEffectController(BaseTestCase):
    """Tests for the Effects Controller."""

    def test_should_return_img_when_get_default(self):
        """Ensure the /default route with GET behaves correctly."""
        response = self.client.get('/api/v1/effects/default')
        img_received = Image.open(BytesIO(response.data))
        self.assert_200
        self.assertIsNotNone(img_received)

    def test_should_return_same_img_when_post_default(self):
        """Ensure the /default route with POST behaves correctly."""
        path_img_sent = path.join(self.app.config['ASSETS_DEFAULT_DIR'], 'valentin.jpg')
        with open(path_img_sent, 'rb') as img:
            img_sent_bytes = BytesIO(img.read())
        file = werkzeug.datastructures.FileStorage(
            stream=img_sent_bytes,
            filename='image.jpg',
            content_type='image/jpg'
        )
        response = self.client.post(
            '/api/v1/effects/default',
            data={
                'file': file
            },
            content_type='multipart/form-data'
        )
        self.assert_200

    def test_should_return_error_when_post_with_invalid_content_type(self):
        """Ensure error is thrown when JSON content type is sent"""
        with self.client:
            self.client.post(
                '/api/v1/effects/default',
                data=json.dumps({}),
                content_type='application/json'
            )
        self.assert400


if __name__ == '__main__':
    unittest.main()
