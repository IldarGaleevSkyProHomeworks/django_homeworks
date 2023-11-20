# Домашняя работа 6.4


1. Установите зависимости

``` PowerShell
poetry install
```

2. Создайте базу данных и пропишите настройки подключения в [config/settings.py](config/settings.py#L86-L93)

3. Примените миграции

``` PowerShell 
 python .\manage.py migrate
```

4. Создайте учетную запись администратора

``` PowerShell
python .\manage.py createsuperuser
```

5. Заполните базу, используя команду `mainfill`

``` PowerShell
python .\manage.py mainfill
```

6. Запустите сервер
``` PowerShell
python .\manage.py runserver
```

## Переменные окружения

### Postgres

| Переменная  | Файл настроек                            | Назначение                          |
|-------------|------------------------------------------|-------------------------------------|
| PG_NAME     | [config/settings.py](config/settings.py) | Имя базы данных                     |
| PG_USER     | [config/settings.py](config/settings.py) | Имя пользователя для подключения    |
| PG_PASSWORD | [config/settings.py](config/settings.py) | Пароль пользователя для подключения |
| PG_HOST     | [config/settings.py](config/settings.py) | Имя хоста с сервером                |
| PG_PORT     | [config/settings.py](config/settings.py) | Порт сервера                        |


### Страница товаров

| Переменная            | Файл настроек                | Назначение                     |
|-----------------------|------------------------------|--------------------------------|
| MAIN_CATALOG_PER_PAGE | [main/apps.py](main/apps.py) | Количество товаров на странице |