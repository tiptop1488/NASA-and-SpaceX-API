import telegram
import os
from dotenv import load_dotenv
import pathlib
import random
import argparse


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['TELEGRAM_TOKEN']
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
        bot.send_photo(chat_id='-1001870496925', photo=contents)
    else:
        path_to_photo = f'images/{name_photo}'
        with open(path_to_photo, 'rb') as f:
            contents = f.read()
        bot.send_photo(chat_id='-1001870496925', photo=contents)
