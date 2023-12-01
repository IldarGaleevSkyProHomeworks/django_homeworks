# Домашняя работа 6.5

<div align="center">
<a href="https://wakatime.com/@IldarGaleev/projects/fereckcopm"><img src="https://wakatime.com/badge/user/45799db8-b1f8-4627-9264-2c8d4c352567/project/018beb28-96ef-4887-b044-66638d506f2f.svg" alt="wakatime"></a>
<img src="https://img.shields.io/github/last-commit/IldarGaleevSkyProHomeworks/django_homeworks.svg"/>
</div>

1. Установите зависимости

``` PowerShell
poetry install
```

2. Создайте базу данных и пропишите настройки подключения в файле .env ([шаблон файла](.env.template))
3. Задайте необходимые [переменные окружения](#переменные-окружения)
4. Примените миграции


> [!IMPORTANT]
> 
> Если перед этим была развернута БД к предыдущим версиям. (Для первичной установки действия из примечания не требуются) 
> 
> Для миграции с версии [homework_6_5](https://github.com/IldarGaleevSkyProHomeworks/django_homeworks/tree/homework_6.5) на текущую необходимо:
> 
> 1. Переименовать таблицу `store_app_contact` в `main_app_contact`
> 2. В таблице `django_content_type` запись `app_label='store_app'|model='contact'` задать значение поля `app_label` в __*main_app*__
> 3. В таблице `django_migrations`
>    - В записи `app='store_app'|name='0003_alter_product_preview_image'` значение поля `name` задать в __*0002_alter_product_preview_image*__
>    - В записи `app='store_app'|name='0002_contact'` значение поля `app` задать в __*main_app*__, а `name` - __*0001_initial*__
> 
>  Эквивалентный SQL код для `Postgres`
> 
> ```postgresql
>   -- 1 --
>   ALTER TABLE store_app_contact RENAME TO main_app_contact;
>   -- 2 --
>   UPDATE django_content_type SET app_label='main_app' WHERE app_label='store_app' AND model='contact';
>   -- 3 --
>   UPDATE django_migrations SET name='0002_alter_product_preview_image' WHERE app='store_app' AND name='0003_alter_product_preview_image';
>   UPDATE django_migrations SET app='main_app', name='0001_initial' WHERE app='store_app' AND name='0002_contact';
> ```
> 
> Либо задайте имя базы данных отличным от предыдущей установки и после применения миграций перенесите необходимые данные вручную.
> 
> __P.S.__ миграция с более ранних версий не рекомендуется.
> Для начала пройдите процедуру миграции к версии [homework_6_5](https://github.com/IldarGaleevSkyProHomeworks/django_homeworks/tree/homework_6.5).

``` PowerShell 
 python .\manage.py migrate
```

5. Создайте учетную запись администратора

``` PowerShell
python .\manage.py createsuperuser
```

6. Заполните базу, используя команды `mainfill` и `productfill`

``` PowerShell
python .\manage.py mainfill
python .\manage.py product
```

7. Запустите сервер
``` PowerShell
python .\manage.py runserver
```
8. Запустите менеджер фоновых задач для отправки e-mail сообщений
``` PowerShell
python .\manage.py process_tasks
```

## Команды

### mainfill

Заполняет таблицу с контактами и товарами

```PowerShell
python .\manage.py mainfill
```

### generatearticles

Генерирует статьи для блога

#### Аргументы

- `count` - позиционный аргумент. Указывает сколько статей сгенерировать. По-умолчанию: 1
- `-p`, `--publish` - опубликовать сгенерированные статьи

```PowerShell
# создать и опубликовать 15 статей
python .\manage.py generatearticles 15 -p
```

### process_tasks

Запуск менеджера фоновых задач для отправки сообщений на почту

```PowerShell
python .\manage.py process_tasks
```

## Переменные окружения

> [!TIP]
> 
> Поддерживается файл `.env` для назначения переменных. [Шаблон файла](.env.template)
> 

### Postgres

| Переменная    | Файл настроек                            | Назначение                          |
|---------------|------------------------------------------|-------------------------------------|
| `PG_NAME`     | [config/settings.py](config/settings.py) | Имя базы данных                     |
| `PG_USER`     | [config/settings.py](config/settings.py) | Имя пользователя для подключения    |
| `PG_PASSWORD` | [config/settings.py](config/settings.py) | Пароль пользователя для подключения |
| `PG_HOST`     | [config/settings.py](config/settings.py) | Имя хоста с сервером                |
| `PG_PORT`     | [config/settings.py](config/settings.py) | Порт сервера                        |


### Страница товаров

| Переменная                                             | Файл настроек                          | Назначение                     |
|--------------------------------------------------------|----------------------------------------|--------------------------------|
| `STORE_CATALOG_PER_PAGE` <sup>[1](#old_per_page)</sup> | [store_app/apps.py](store_app/apps.py) | Количество товаров на странице |


### Страница публикаций

| Переменная                     | Файл настроек                        | Назначение                                                                                                                |
|--------------------------------|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| `ARTICLES_PER_PAGE`            | [blog_app/apps.py](blog_app/apps.py) | Количество публикаций на странице                                                                                         |
| `ARTICLE_VIEW_COUNTS_CONGRATS` | [blog_app/apps.py](blog_app/apps.py) | Количество просмотров публикации, при котором отсылаестя сообщение. Переменная содержит список чисел, разделенных запятой |


### Background worker

| Переменная            | Файл настроек                            | Назначение                                      |
|-----------------------|------------------------------------------|-------------------------------------------------|
| `BGTASK_MAX_ATTEMPTS` | [config/settings.py](config/settings.py) | Количество попыток повторного выполнения задачи |


## Логирование

Для настройки логирования укажите путь к json файлу конфигурации в переменной окружения `LOGGING_CONFIG_FILE`.

Пример файла конфигурации для вывода отладочных сообщений в консоль от менеджера фоновых задач:

```json
{
  "version": 1,
  "disable_existing_loggers": false,
  "handlers": {
    "console": {
      "class": "logging.StreamHandler"
    }
  },
  "root": {
    "handlers": [
      "console"
    ],
    "level": "WARNING"
  },
  "loggers": {
    "tasks.send_mail": {
      "level": "DEBUG"
    }
  }
}
```

---

<a name="old_per_page">1</a> - в предыдущих версиях MAIN_CATALOG_PER_PAGE