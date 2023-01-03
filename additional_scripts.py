import requests
import distutils.dir_util
from urllib.parse import urlparse
import os


def get_image(image_link, image_save_path, payload=None):
    distutils.dir_util.mkpath('images')
    response = requests.get(image_link, params=payload)
    response.raise_for_status()
    image_save_path = os.path.join('images', image_save_path)
    with open(image_save_path, 'wb') as file:
        file.write(response.content)


def get_format_file(image_link):
    description = urlparse(image_link)
    file_format = os.path.splitext(description.path)[1]
    return file_format
