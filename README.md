# Indications
Это демонстрационный проект созданый для ознакомления и оценки данного проекта.
Проект про телеграм бота который принимает показания счётчика газа дистанционо.


Для того чтобы протестировать проект нужно создать свою виртуальную среду:

python -m venv env

После чего её нужно активировать:

source env/bin/activate

Далее переходим в директорию на уровень ниже под названием Indications и устанавливаем все зависимости:

cd Indications
pip install -r requirements.txt

В случае отсутствия в системе Redis, его нужно будет установить.
Убедиться в его наличии можно командой redis-cli
И если у Вас он есть то можно будет наблюдать подобное:

127.0.0.1:6379>

А если нету, то выполните ряд команд:

curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis

После установки Redis, нужно создать в админке хотябы по одному экземляру каждой модели кроме Indication.
Для это сперва нужно запустить сервер из директории с файлом manage.py

python manage.py runserver

Далее нужно создать главного пользователя в админке

python manage.py createsuperuser

И авторизироваться по ссылке http://127.0.0.1:8000/admin
После чего создать те самые экземляры моделей

Далее в одной вкладке терминала запускаем сервер с воркером celery

celery -A Indications worker

A во второй запустить файл telegrambot.py

Если после запуска вы ничего не увидите, то это признак того, что файл работает корректно
Поздравляю! Проект запущен!
