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
    chat_id = os.environ['CHAT_ID']
    bot = telegram.Bot(token=token)
    currentDirectory = pathlib.Path('images')
    name_images = []
    for currentFile in currentDirectory.iterdir():
        name_images.append(currentFile)
    parser = argparse.ArgumentParser()
    parser.add_argument('--time_sleep')
    args = parser.parse_args()
    if args.time_sleep:
        time_sleep = ((int(args.time_sleep)) * 60) * 60
    else:
        time_sleep = 4 * 60 * 60
    while True:
        images = name_images
        for i in images:
            with open(i, 'rb') as f:
                contents = f.read()
            bot.send_photo(chat_id=chat_id, photo=contents)
            time.sleep(time_sleep)
        random.shuffle(images)
