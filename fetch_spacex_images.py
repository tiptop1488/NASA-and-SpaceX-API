import requests
import additional_scripts
import argparse


def fetch_spacex_last_launch(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    description = response.json()
    image_links = description['links']['flickr']['original']
    for link_number, link in enumerate(image_links):
        print(link_number, link)
        format_file = additional_scripts.get_format_file(link)
        additional_scripts.get_image(link, f"SPACEX_{link_number}.{format_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_id', default='latest')
    args = parser.parse_args()
    launch_id = args.launch_id
    try:
        fetch_spacex_last_launch(launch_id)
    except requests.exceptions.HTTPError as err:
        print(err.response.status_code)
        print(err.response.text)
