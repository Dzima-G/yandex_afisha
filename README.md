# Афиша мест

Яндекс Афиша на Django, серверная часть.

## Запуск

Для запуска у вас уже должен быть установлен Python 3.13

- Скачайте код
- Виртуальное окружение (команды выполняются в терминале):  
  - Создайте виртуальное окружение, заменить путь на фактический к проекту (см. документацию https://docs.python.org/3/library/venv.html):
  ```python
  python -m venv C:\path\MyProject\venv
  ```   
  - Активируйте виртуально окружение из папки вашего проекта, Пример: `PS C:\path\MyProject> venv\Scripts\activate`:
  ```python
  venv\Scripts\activate
  ```
- Установите зависимости:
  ```python
  pip install -r requirements.txt
  ```
- Проверка установленных зависимостей:
  ```python
  pip freeze
  ```
- Выполните миграцию:
  ```python
  python manage.py migrate
  ```
- Запустите сервер:
  ```python
  python manage.py runserver
  ```

После этого переходите по ссылке [127.0.0.1:8000](http://127.0.0.1:8000), вы увидите главную страницу.

Для входа в панель администратора:

- Создание суперпользователя:
  ```python
  python manage.py createsuperuser
  ```
- Запустите сервер командой 
  ```python
  python manage.py runserver
  ```
Переходите по ссылке [127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/), вы увидите вход в панель администратора.

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

**Для запуска проекта необходима обязательная настройка**.
Переменные:
- секретный ключ проекта. Например: `erofheronoirenfoernfx49389f43xf3984xf9384`:
  ```python
  SECRET_KEY
  ```

**Для запуска проекта эти настройки не требуются**, значения уже проставлены по умолчанию.

Доступны следущие переменные:
- дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. Выключается значением `False`:
  ```python
  DEBUG
  ```
- имя хоста / домена, которые может обслуживать этот сайт см. [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts):
  ```python
  ALLOWED_HOSTS
  ```
Пример сайта можно посмотреть по ссылке: https://dzima.pythonanywhere.com/

**Добавление новых мест с помощью GeoJSON:**
- требуется файл формата json (GeoJSON) см. https://ru.wikipedia.org/wiki/GeoJSON (образец [sample place.json](https://github.com/Dzima-G/yandex_afisha/blob/main/sample%20place.json))
- для запуска добавления места (URL - ссылка на файл GeoJSON): 
  ```python
  python manage.py load_place URL
  ```   

Пример запуска:
  ```python
  python manage.py load_place https://raw.githubusercontent.com/Dzima-G/yandex_afisha/refs/heads/main/static/places/moscow_legends.json
  ```
## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
