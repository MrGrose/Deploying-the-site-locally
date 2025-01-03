# Пульт охраны банка
Это внутренний репозиторий для сотрудников банка "Сияние". Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у Вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пуль охраны - это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.


### Как установить
Перед тем как использовать скрипт, убедитесь, что у вас настроено виртуальное окружение.

1. Создайте файл .env в корневой директории проекта со следующим содержимым:

    ```bash
    SECRET_KEY=ваш_секретный_ключ
    HOST=ваш_хост
    PORT=ваш_порт
    NAME=ваше_имя
    USER=ваш_пользователь
    PASSWORD=ваш_пароль
    LANGUAGE_CODE=ваш_языковой_код
    TIME_ZONE=ваша_временная_зона
    DEBUG=ваше_значение_true_или_false
    ```


2.  Python3 должен быть уже установлен. Затем pip(или pip3есть конфликт с Python2) для установки зависимостей:

    ```bash
    pip install -r requirements.txt
    ```


### Использование
1. Запуск скрипта (запускает сервер с вашим сайтом на localhost).Вы так же можете заменить 0.0.0.0:8000 на удобные вам данные.
    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```
    При успешном запуске:

    ```bash
    System check identified no issues (0 silenced).
    December 24, 2024 - 12:50:14
    Django version 3.2.25, using settings 'project.settings'
    Starting development server at http://0.0.0.0:8000/
    Quit the server with CTRL-BREAK.
    ```

### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org .