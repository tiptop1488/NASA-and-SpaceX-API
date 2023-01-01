import requests
from dotenv import load_dotenv
import os
import additional_scripts
import datetime
import argparse


def get_nasa_epic_image(api_key, date):
    if not date:
        date = '2022-12-13'
    year, month, day = date.split('-')
    user_date = datetime.datetime(year=int(year), month=int(month), day=int(day))
    payload = {'api_key': api_key}
    url = f'https://api.nasa.gov/EPIC/api/natural/date/{user_date}'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    content = response.json()
    image_links = []
    for description in content:
        image_name = description['image']
        new_date = user_date.strftime("%Y/%m/%d")
        url = f'https://api.nasa.gov/EPIC/archive/natural/{new_date}/png/{image_name}.png'
        image_links.append(url)
    for link_number, link in enumerate(image_links):
        format_file = additional_scripts.get_format_file(link)
        additional_scripts.get_image(link, f"NASA_EPIC_{link_number}.{format_file}", payload)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser()
    parser.add_argument('--date')
    args = parser.parse_args()
    date = args.date
    get_nasa_epic_image(api_key, date)
