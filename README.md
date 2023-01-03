# Сбор и публикация в телеграм канал фотографии космоса и запуска ракет

Набор скриптов предназначен для скачивания и последующей отправки в телеграмм канал: 
* фотографий космоса и земли, сделанных NASA 
* фотографий с запуска ракет SpaceX

## Установка

Для запуска потребуется `python 3` и библиотеки перечисленные в файле `requirements.txt`. Для установки используйте команду:

```
pip install -r requirements.txt
```

Все файлы запускаются по отдельности, кроме `additional_scripts.py`, в нем хранятся вспомогательные скрипты.
Все скачанные фотографии сохраняются в в директорию `images`. Если данной директории нет в проекте - она создастся автоматически.
Так же вам потребуется создать файл `.env` и добавить переменные окружения.

```
NASA_API_KEY = 'ваш ключ API для работы с NASA'
TELEGRAM_TOKEN = 'токен вашего телеграмм бота'
TG_CHAT_ID = 'id канала для публикаций'
```

## fetch_nasa_apod_images.py

Скачивает в директорию `images` фотографии космоса от NASA серии APOD. Принимает один необязательный аргумент - количество фотографий. По умолчанию будет скачано 30 фотографий.

```
python3 fetch_nasa_apod_images.py --count 30
```

## fetch_nasa_epic_images.py

Скачивает в директорию `images` фотографии земли от NASA серии EPIC. Принимает один необязательный аргумент - дата создания снимков. По умолчанию будет использована дата - '2022-12-13'.

```
python fetch_nasa_epic_images.py --date 2022-10-13
```

## fetch_spacex_images.py

Скачивает в директорию `images` фотографии с запуска ракет SpaceX. Принимает на вход один необязательный аргумент - id запуска. Если id не указан, скачает фотографии последнего запуска. Если на последнем запуске фотографии не делались, скачает фотографии запуска-примера.

```
python3 fetch_spacex_images.py --launch_id 5eb87d47ffd86e000604b38a
```

## telegram_sender_bot.py

Отправляет фотографию в телеграмм канал. На вход принимает один необязательный элемент - название фотографии.
Если фотография не найдена или аргумент не указан опубликует рандомную фотографию из тех что есть в директории `images`.

```
python3 telegram_sender_bot.py --name_photo NASA_8.jpg
```

## telegram_endless_sender_bot.py

По очереди отправляет фотографии из директории `images` в телеграмм канал. Если отправленные все фотографии, продолжает публиковать снимки в рандомном порядке.
На вход принимает один необязательный элемент - время между публикациями. Время указывается в часах. Если аргумент не передан, стандартная задержка между публикациями составляет 4 часа.

```
python3 telegram_endless_sender_bot.py --time_slip 1
```

## additional_scripts.py

Набор функций для работы с API spaceX и NASA которые используются в описанных ранее скриптах.

