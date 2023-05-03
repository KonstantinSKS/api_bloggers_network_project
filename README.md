# api_final_yatube
## Описание:
API для Yatub представляет собой backend-проект социальной сети, в которой пользователи имеют возможность
публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов, выполнять поиск по подпискам.

## Технологии:
- Python 3.7
- Django 3.2
- djangorestframework
- JWT + Djoser

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/KonstantinSKS/api_final_yatube.git
```
```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```

После запуска сервера документация к API будет доступна по ссылке:
http://127.0.0.1:8000/redoc/

## Примеры запросов к API:

**GET- запросы:**

эндпоинт /api/v1/posts/ - Получить список всех публикаций.

эндпоинт /api/v1/posts/{id}/ - Получение публикации по id.

эндпоинт /api/v1/posts/{post_id}/comments/ - Получение всех комментариев к публикации.

**POST- запросы**
- эндпоинт /api/v1/posts/ - Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.

в body:
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

- эндпоинт /api/v1/jwt/create/ - Получение JWT-токена.

в body:
```
{
  "username": "string",
  "password": "string"
}
```

Подробную документация к API проекта Yatube и примеры смотри на /redoc/


Автор: Стеблев Константин
