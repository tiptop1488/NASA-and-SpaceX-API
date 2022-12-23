import telegram
import os
from dotenv import load_dotenv
import pathlib
import random
import argparse


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['CHAT_ID']
    bot = telegram.Bot(token=token)
    currentDirectory = pathlib.Path('images')
    name_images = []
    for currentFile in currentDirectory.iterdir():
        name_images.append(currentFile)
    parser = argparse.ArgumentParser()
    parser.add_argument('--name_photo')
    args = parser.parse_args()
    name_photo = args.name_photo
    if not name_photo:
        name_photo = random.choice(name_images)
        with open(name_photo, 'rb') as f:
            contents = f.read()
        bot.send_photo(chat_id=chat_id, photo=contents)
    else:
        path_to_photo = f'images/{name_photo}'
        with open(path_to_photo, 'rb') as f:
            contents = f.read()
        bot.send_photo(chat_id=chat_id, photo=contents)
