import telegram
import os
from dotenv import load_dotenv
import pathlib
import random
import argparse


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    bot = telegram.Bot(token=token)
    current_directory = pathlib.Path('images')
    name_images = []
    for current_file in current_directory.iterdir():
        name_images.append(current_file)
    parser = argparse.ArgumentParser()
    parser.add_argument('--name_photo')
    args = parser.parse_args()
    name_photo = args.name_photo
    if not name_photo:
        path_to_photo = random.choice(name_images)
    else:
        path_to_photo = os.path.join('images', name_photo)
    with open(path_to_photo, 'rb') as f:
        contents = f.read()
    bot.send_photo(chat_id=chat_id, photo=contents)
