import telegram
import os
from dotenv import load_dotenv
import pathlib
import time
import random
import argparse

if __name__ == '__main__':
    load_dotenv()
    token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    bot = telegram.Bot(token=token)
    current_directory = pathlib.Path('images')
    name_images = [current_file for current_file in current_directory.iterdir()]
    parser = argparse.ArgumentParser()
    parser.add_argument('--time_sleep')
    args = parser.parse_args()
    if args.time_sleep:
        time_sleep = ((int(args.time_sleep)) * 60) * 60
    else:
        time_sleep = 4 * 60 * 60
    while True:
        images = name_images
        for image in images:
            with open(image, 'rb') as f:
                contents = f.read()
            try:
                bot.send_photo(chat_id=chat_id, photo=contents)
                time.sleep(time_sleep)
            except telegram.error.NetworkError:
                time.sleep(10)
        random.shuffle(images)


