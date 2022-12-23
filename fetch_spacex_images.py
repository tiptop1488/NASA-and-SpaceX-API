import requests
import additional_scripts
import argparse


def fetch_spacex_last_launch(launch_id):
    if launch_id:
        url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    else:
        url = 'https://api.spacexdata.com/v5/launches/latest'
    response = requests.get(url)
    if not response.ok:
        launch_id = '5eb87d47ffd86e000604b38a'
        fetch_spacex_last_launch(launch_id)
        image_links = []
    else:
        description = response.json()
        image_links = description['links']['flickr']['original']
    if not image_links:
        launch_id = '5eb87d47ffd86e000604b38a'
        fetch_spacex_last_launch(launch_id)
    else:
        image_links = enumerate(image_links)
    for i in image_links:
        additional_scripts.get_image(i[1], f"spaceX_{i[0]}.jpeg")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_id')
    args = parser.parse_args()
    launch_id = args.launch_id
    fetch_spacex_last_launch(launch_id)