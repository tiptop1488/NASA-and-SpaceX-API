import requests
from dotenv import load_dotenv
import os
import additional_scripts
import argparse


def get_nasa_apod_image(api_key, count=30):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': api_key, 'count': count}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    content = response.json()
    image_links = [description['url'] for description in content if description['media_type'] == 'image']
    for link_number, link in enumerate(image_links):
        format_file = additional_scripts.get_format_file(link)
        additional_scripts.get_image(link, f"NASA_APOD_{link_number}.{format_file}", api_key)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser()
    parser.add_argument('--count')
    args = parser.parse_args()
    count = args.count
    get_nasa_apod_image(api_key, count)
