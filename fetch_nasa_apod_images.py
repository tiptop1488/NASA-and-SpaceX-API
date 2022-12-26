import requests
from dotenv import load_dotenv
import os
import additional_scripts


def get_nasa_apod_image(api_key):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': api_key, 'count': 30}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    content = response.json()
    image_links = []
    for description in content:
        if description['media_type'] == 'image':
            image_links.append(description['url'])
    image_links = enumerate(image_links)
    for link in image_links:
        additional_scripts.get_image(link[1], f"NASA_{link[0]}.{additional_scripts.get_format_file(link[1])}", api_key)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    get_nasa_apod_image(api_key)
