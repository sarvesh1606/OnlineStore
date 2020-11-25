# OnlineStore
Python web application where user can place order of desired items. Developed features like social login, single page functionality ,both administrator and client side user authentication.

## - A Django application

Please be sure you have installed pip and Django in your system.

Please follow following steps

1. First step is to create migration files using the following command:
```buildoutcfg
python manage.py makemigrations
```

2. Then migrate using the following command:
```buildoutcfg
python manage.py migrate
```

3. Create super user using the command:
```
python manage.py createsuperuser
```
enter your username, email and password

4. run server using the command:
```
python manage.py runserver
```
5. visit admin panel at `127.0.0.1:8000/admin` 
