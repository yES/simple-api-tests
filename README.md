# simple-api-tests

## Установка глобальных пакетов
    sudo apt-get install python-setuptools
    sudo easy_install pip
    sudo pip install virtualenv

## Установка окружения
    git clone git@github.com:yES/simple-api-tests.git
    cd simple-api-tests
    virtualenv env
    env/bin/pip install -r requirements.txt

## Запуск тестового сервера
    env/bin/python api_server.py
   
## Запуск тестов
    env/bin/python -m unittest tests.format tests.functional tests.negative
