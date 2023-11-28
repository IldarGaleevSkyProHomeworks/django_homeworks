# Домашняя работа 6.4


1. Установите зависимости

``` PowerShell
poetry install
```

2. Создайте базу данных и пропишите настройки подключения в [config/settings.py](config/settings.py#L86-L93)

3. Примените миграции

> [!IMPORTANT]
> 
> Если до этого была развернута БД под версию [homework_6_4](https://github.com/IldarGaleevSkyProHomeworks/django_homeworks/tree/homework_6.4) и раньше.
> Перед применением миграций выполните команду:
> 
> ```PowerShell
> python .\manage.py rename_app main store_app
> ```
> 
> чтобы перенести данные из предыдущей версии.

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

| Переменная                                           | Файл настроек                          | Назначение                     |
|------------------------------------------------------|----------------------------------------|--------------------------------|
| STORE_CATALOG_PER_PAGE <sup>[1](#old_per_page)</sup> | [store_app/apps.py](store_app/apps.py) | Количество товаров на странице |

---

<a name="old_per_page">1</a> - в предыдущих версиях MAIN_CATALOG_PER_PAGE