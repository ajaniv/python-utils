#/usr/bin/env python
# -#- coding: utf-8 -#-

#
# omcore/utils/tests/test_image_util.py - image utilities test cases
#
# This file is part of Obelius Media  Ad-Server  components
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
#
# Copyright (C) 2013-2014 Obelius Media
#

# Initial version: 2013-11-26
# Author: Amnon Janiv <amnon.janiv@obeliusmedia.com>

"""

..  module:: omcore.utils.tests.test_image_util.py
    :synopsis: image utilities module  test cases




.. moduleauthor:: Amnon Janiv <amnon.janiv@obeliusmedia.com>

"""

from PIL import Image

import io
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


from omcore.utils import image_util
from omcore.utils.tests.test_util import BaseAppDjangoTestCase

CODEC = image_util.DEFAULT_CODEC_NAME

class ImageTestCase(BaseAppDjangoTestCase):
    """
    Python image test case base class
    """

    def setUp(self):
        super(ImageTestCase, self).setUp()
        self.read_image = image_util.read_image(
            os.path.join(DATA_DIR, self.image_file_name))

    def encode_check(self):
        encoded_image = image_util.encode(self.read_image, CODEC)
        decoded_image = image_util.decode(encoded_image, CODEC)
        self.assertTrue(len(self.read_image) == len(decoded_image),
                        "Invalid decoded image")
        self.assertTrue(self.read_image == decoded_image)
        image_before = Image.open(io.BytesIO(self.read_image))
        image_after = Image.open(io.BytesIO(decoded_image))
        image_util.diff(image_before, image_after)


class PngImageTestCase(ImageTestCase):
    """
    PNG image test case  class
    """

    image_file_name = 'image.png'

    def test_base64_encoding(self):
        self.encode_check()


class JpegImageTestCase(ImageTestCase):
    """
    JPEG image test case  class
    """

    image_file_name = 'image.jpeg'

    def test_base64_encoding(self):
        self.encode_check()


class GifImageTestCase(ImageTestCase):
    """
    GIF image test case  class
    """

    image_file_name = 'image.gif'

    def test_base64_encoding(self):
        self.encode_check()
