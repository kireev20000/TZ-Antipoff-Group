# TZ-Antipoff-Group
Тестовое задание на стажировку.

---
## Технологии
- Python 3.9
- Django 4.2
- SQLite
- django_rest_framework 3.12.4
- django-filter 22.1

---
## Запуск проекта:
Клонировать репозиторий
```sh
git clone git@github.com:kireev20000/TZ-Antipoff-Group.git
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Запустить локальный сервер
```
python manage.py runserver 8000
```
## Документация
### Документация в формате OpenAPI 3.0 доступна по адресу
http://127.0.0.1:8000/api/schema/swagger-ui/

---
### Данные для входа админку:
```
login = admin
password = 12345
```
---
### Парочка простых тестов для проверки (для примера)
```
python manage.py test api
```
---
### В корне репозитория лежит коллекция запросов для Postman.
```
TZ-Antipoff-Group.postman_collection.json
```
###
Запуск докера
```
docker build --tag python-django .
docker run --publish 8000:8000 python-django
```