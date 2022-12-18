import requests


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(url)
    response.raise_for_status()
    description = response.json()
    image_links = description['links']['flickr']['original']
    image_links = enumerate(image_links)
    for i in image_links:
        get_image(i[1], f"spaceX_{i[0]}.jpeg")