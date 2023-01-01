import requests
from dotenv import load_dotenv
import os
import additional_scripts
import datetime


def get_nasa_epic_image(api_key):
    user_date = datetime.datetime(year=2022, month=12, day=13) #'2022-12-13'
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
    get_nasa_epic_image(api_key)
