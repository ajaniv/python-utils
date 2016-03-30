"""
.. module::  utils.image
   :synopsis:  Image  utilities module.

The *image* module contains a collection of image helper functions
and classes.


"""

import base64
import PIL

DEFAULT_CODEC_NAME = 'base64'


def load(file_path):
    """
    Create an Image instance from a file
    """
    image = PIL.Image.open(file_path)
    return image


def read_image(file_path):
    """
    Read an image file
    """
    with open(file_path, "rb") as ifile:
        return ifile.read()


def encode_file(file_handle, encoder_name=DEFAULT_CODEC_NAME):
    """
    Encode file stream
    """
    try:
        file_handle.seek(0)
        data = encode(file_handle.read(), encoder_name)
    except ValueError:
        if file_handle.closed:
            with open(file_handle.name, "rb") as image_file:
                data = encode(image_file.read(), encoder_name)
        else:
            raise

    return data


def encode_path(file_path, encoder_name=DEFAULT_CODEC_NAME):
    """
    Encode file path
    """

    return encode(read_image(file_path), encoder_name)


def encode(image_data, encoder_name):
    """
    Image encoding from binary data
    """
    if encoder_name == DEFAULT_CODEC_NAME:
        return base64.b64encode(image_data)
    raise ValueError('Invalid codec name %s' % encoder_name)


def decode(encoded_data, decoder_name=DEFAULT_CODEC_NAME):
    """
    Image decoding from binary data
    """
    if decoder_name == DEFAULT_CODEC_NAME:
        return base64.b64decode(encoded_data)
    raise ValueError('Invalid codec name %s' % decoder_name)


def diff(image1, image2):
    """
    High order image comparison - further accuracy required
    """
    def check_format():
        """Verify image format.
        """
        if image1.format != image2.format:
            msg = 'Different image formats {} {}'
            raise ValueError(msg.format(image1.format, image2.format))

    def check_size():
        """Verify image size.
        """
        if image1.size != image2.size:
            msg = 'Different image size {} {}'
            raise ValueError(msg.format(image1.size, image2.size))

    def check_raw_data():
        """Verify contents.
        """
        bytes1 = image1.tobytes()
        bytes2 = image2.tobytes()
        if len(bytes1) != len(bytes2) or bytes1 != bytes2:
            msg = 'Different image contents'
            raise ValueError(msg.format())

    for check_fn in (check_format, check_size, check_raw_data):
        check_fn()
