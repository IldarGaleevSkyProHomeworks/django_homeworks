# Домашняя работа 6.3


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
