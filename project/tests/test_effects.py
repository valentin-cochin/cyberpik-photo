import unittest
from io import BytesIO
from os import path

from PIL import Image, ImageChops
from project.tests.base import BaseTestCase


class TestEffectController(BaseTestCase):
    """Tests for the Effects Controller."""

    def test_should_return_default_image_when_get_default_route(self):
        """Ensure the /default route with GET behaves correctly."""
        response = self.client.get('/api/v1/effects/default')
        img_received = Image.open(BytesIO(response.data))
        self.assert_200
        self.assertIsNotNone(img_received)


def for_later():
    pass
    # path_img_expected = path.join(self.app.config['ASSETS_DEFAULT_DIR'], 'valentin.jpg')
    # img_expected = Image.open(path_img_expected).convert('RGB')


if __name__ == '__main__':
    unittest.main()
