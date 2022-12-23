import requests
from dotenv import load_dotenv
import os
import additional_scripts


def get_nasa_epic_image():
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    date = '2022-12-13'
    payload = {'api_key': api_key}
    url = f'https://api.nasa.gov/EPIC/api/natural/date/{date}'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    description = response.json()
    images_links = []
    for i in description:
        image_name = i['image']
        date = date.replace('-', '/')
        url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image_name}.png'
        images_links.append(url)
    images_links = enumerate(images_links)
    for i in images_links:
        additional_scripts.get_image(i[1], f"NASA_EPIK_{i[0]}.{additional_scripts.get_format_file(i[1])}")


if __name__ == '__main__':
    get_nasa_epic_image()