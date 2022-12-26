import requests
import distutils.dir_util
from urllib.parse import urlparse
import os


def get_image(image_link, image_save_path, api_key=None):
    distutils.dir_util.mkpath('images')
    if 'EPIC' in image_link:
        payload = {'api_key': api_key}
        url = image_link
        response = requests.get(url, params=payload)
    else:
        url = image_link
        response = requests.get(url)
    response.raise_for_status()
    image_save_path = os.path.join('images', image_save_path)
    with open(image_save_path, 'wb') as file:
        file.write(response.content)


def get_format_file(image_link):
    description = urlparse(image_link)
    file_format = os.path.splitext(description.path)[1]
    return file_format
