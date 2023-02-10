# django_project
[![Python package](https://github.com/G1ebS/django_project/actions/workflows/python-package.yml/badge.svg?branch=master)](https://github.com/G1ebS/django_project/actions/workflows/python-package.yml)

Привет, это мой первый проект на Django.
Ссылка для клонирования: https://github.com/G1ebS/django_project.git (для командной строки - gh repo clone G1ebS/django_project)
Создание и активация виртуальной среды venv с помощью командной строки:
- python -m venv
- cd venv/scripts
- /.activate (/.deactivate - если вы хотите деактивировать)
Установка необходимых библиотек для использования
- pip install -r requirements.txt
## Чтобы запустить проект в dev-режиме - нужно:
1. Запустить терминал
2. Установить requirements-dev.txt (pip install -r requirements-dev.txt)
3. Перейти в директорию с файлом manage.py (cd django_project)
4. Прописать: python manage.py runserver
## Как запустить сервер со своим env?
Создать файл .env в папке с файлом settings.py (путь: /django_project/django_project), где должны быть прописаны следующие параметры:
- SECRET_KEY: что-то типо такого w^zag_-i^mbvq96$e-$l9b)ve)7f4p4#ein1vsl^=qx_s6=ukl - это значение и будет в проекте по умолчанию
- DEBUG: True или False (по умолчанию будет значение True)
- ALLOWED_HOSTS: набор хостов, через запятую + пробел, например ALLOWED_HOSTS=some_host.com, some_host1.com (по умолчанию будет будет указана * - то есть все хосты)

***Образец заполнения .env файла представлен в файле .env.example***