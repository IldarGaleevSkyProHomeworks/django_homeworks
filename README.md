# Домашняя работа 6.5

<div align="center">
<a href="https://wakatime.com/@IldarGaleev/projects/fereckcopm"><img src="https://wakatime.com/badge/user/45799db8-b1f8-4627-9264-2c8d4c352567/project/018beb28-96ef-4887-b044-66638d506f2f.svg" alt="wakatime"></a>
<img src="https://img.shields.io/github/last-commit/IldarGaleevSkyProHomeworks/django_homeworks.svg"/>
</div>

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

6. Задайте необходимые [переменные окружения](#переменные-окружения)

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