Установка
Клонировать репозиторий и перейти в него в командной строке:

git clone <git link>
cd api_final_yatube
Cоздать и активировать виртуальное окружение:

python -m venv env
source env/bin/activate
python -m pip install --upgrade pip
Установить зависимости из файла requirements.txt:

pip install -r requirements.txt
Выполнить миграции:

python manage.py migrate
Запустить проект:

python manage.py runserver