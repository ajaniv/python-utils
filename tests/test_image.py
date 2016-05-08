"""
..  module:: tests.test_image.py
    :synopsis: image utilities unit test module.
image utilities unit test module
"""

from __future__ import absolute_import
import io
import os
import unittest
from PIL import Image
from python_core_utils import image

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


CODEC = image.DEFAULT_CODEC_NAME


class BaseImageTestCase(unittest.TestCase):
    """
    Python image test case base class
    """

    def setUp(self):
        super(BaseImageTestCase, self).setUp()
        self.read_image = image.read_image(
            os.path.join(DATA_DIR, self.image_file_name))

    def encode_check(self):
        encoded_image = image.encode(self.read_image, CODEC)
        decoded_image = image.decode(encoded_image, CODEC)
        self.assertTrue(len(self.read_image) == len(decoded_image),
                        "Invalid decoded image")
        self.assertTrue(self.read_image == decoded_image)
        image_before = Image.open(io.BytesIO(self.read_image))
        image_after = Image.open(io.BytesIO(decoded_image))
        image.diff(image_before, image_after)


class ImageTestCase(BaseImageTestCase):
    """
    GIF image test case  class
    """

    image_file_name = 'image.gif'

    def test_load(self):
        loaded_image = image.load(os.path.join(DATA_DIR, self.image_file_name))
        self.assertTrue(loaded_image)

    def test_encode_file(self):
        with open(os.path.join(DATA_DIR, self.image_file_name),
                  'rb') as image_file:
            encoded_image = image.encode_file(image_file)
            self.assertTrue(encoded_image)


class PngImageTestCase(BaseImageTestCase):
    """
    PNG image test case  class
    """

    image_file_name = 'image.png'

    def test_base64_encoding(self):
        self.encode_check()


class JpegImageTestCase(BaseImageTestCase):
    """
    JPEG image test case  class
    """

    image_file_name = 'image.jpeg'

    def test_base64_encoding(self):
        self.encode_check()


class GifImageTestCase(BaseImageTestCase):
    """
    GIF image test case  class
    """

    image_file_name = 'image.gif'

    def test_base64_encoding(self):
        self.encode_check()
