import requests
import distutils.dir_util
from urllib.parse import urlparse
import os


def get_image(image_link, image_save_path):
    distutils.dir_util.mkpath('images')
    if 'wikimedia' in image_link:
        headers = {'User-Agent': 'tiptop148859@gmail.com'}
        url = image_link
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        with open('images' + '/' + image_save_path + '.jpg', 'wb') as file:
            file.write(response.content)
    if 'EPIC' in image_link:
        payload = {'api_key': ''}
        url = image_link
        response = requests.get(url, params=payload)
        response.raise_for_status()
        with open('images' + '/' + image_save_path, 'wb') as file:
            file.write(response.content)
    else:
        url = image_link
        response = requests.get(url)
        response.raise_for_status()
        with open('images' + '/' + image_save_path, 'wb') as file:
            file.write(response.content)


def get_format_file(image_link):
    description = urlparse(image_link)
    path_to_file = os.path.split(description[2])[1]
    file_format = os.path.splitext(path_to_file)[1][1:]
    return file_format
