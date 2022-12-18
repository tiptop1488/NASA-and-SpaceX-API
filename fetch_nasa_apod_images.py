import requests


def get_nasa_apod_image():
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': '', 'count': 30}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    description = response.json()
    image_links = []
    for i in description:
        image_links.append(i['url'])
    image_links = enumerate(image_links)
    for i in image_links:
        get_image(i[1], f"NASA_{i[0]}.{get_format_file(i[1])}")