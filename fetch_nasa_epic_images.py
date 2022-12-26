import requests
from dotenv import load_dotenv
import os
import additional_scripts


def get_nasa_epic_image(api_key):
    date = '2022-12-13'
    payload = {'api_key': api_key}
    url = f'https://api.nasa.gov/EPIC/api/natural/date/{date}'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    content = response.json()
    images_links = []
    for description in content:
        image_name = description['image']
        date = date.replace('-', '/')
        url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image_name}.png'
        images_links.append(url)
    images_links = enumerate(images_links)
    for link in images_links:
        additional_scripts.get_image(link[1], f"NASA_EPIK_{link[0]}{additional_scripts.get_format_file(link[1])}", api_key)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    get_nasa_epic_image(api_key)