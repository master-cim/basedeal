![](https://img.shields.io/badge/Python-3.7.5-blue) 
![](https://img.shields.io/badge/Django-2.2.16-green)
![](https://img.shields.io/badge/DjangoRestFramework-3.12.4-red)
![](https://img.shields.io/badge/Docker-3.8-yellow)
![](https://img.shields.io/badge/Telegram_message-passing-green)
![](https://github.com/master-cim/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
  
## Название проекта
# БазаДел
## _Агентство инновационных ИТ-решений_

[![Baza|Del](https://sun9-38.userapi.com/s/v1/ig2/NyzOoOIRbTbfNG74Uorihl5NkeN2cve5Ph5I1_PEhF8V1yO_RnkWiO_JSVgVklyq8Q3ahwpFOGWcn5c8pUoao_rk.jpg?quality=95&as=32x33,48x50,72x75,108x112,160x166,240x249,360x373,382x396&from=bu&u=tg9zQqY9rtgcHIXwyik9fwGd7LKPMDXyYeO3Sp7U3Ww&cs=320x332)](https://)

![Static Badge](https://img.shields.io/badge/:badgeContent?style=plastic)


✨ Мы специализируемся на инженирии данных, предоставляя Вам надежные и эффективные решения для управления информацией. Наша команда экспертов также занимается аналитикой данных, помогая Вам превратить огромные объемы информации в ценные и практические знания.

✨ Кроме того, мы создаем современные и интуитивно понятные веб-сайты, телеграмм чат-боты и телеграмм проекты, чтобы помочь Вам эффективно взаимодействовать с Вашими клиентами. 

**Возможности приложения:**  
:black_small_square: Регистрация на сайте, получение токена, изменение данных своей учетной записи  
:black_small_square: Раздаление прав пользователей согласно, назначенной ему роли  
:black_small_square: Возможность, согласно авторизации выполнять следующие дествия: получать, добавлять и удалять - категорию, жанр, произведение, отзыв и комментарий  
:black_small_square: Администрирование пользователями 
## :computer: Технологии в проекте

:small_blue_diamond: Python  
:small_blue_diamond: Django  
:small_blue_diamond: Django REST Framework  
:small_blue_diamond: Docker  
:small_blue_diamond: Continuous Integration  
:small_blue_diamond: Continuous Deployment  
:small_blue_diamond: Telegram notification message  


## :pencil2: Инструкции по запуску
Для того чтобы развернуть образ на локальной машине, выполнитеследующиедействия.
1. Авторизоваться через консоль:
```sh
docker login -u <имя пользователя>
```
2. Загрузка образа с DockerHub
```sh
docker pull mastersup/infra:v1.04.2022
```
3. Проверьте, что образ в системе.
```sh
docker images
```
4. Запустите Докер-контейнер с этим образом:
```sh
docker-compose up -d
```
5. Проверьте в отдельном окне bush состояние контейнера:
```sh
docker ps
```
6. Скопируйте ID контейнера infra_web, используйте команду для доступа информации:
```sh
docker container ls
```
7. Зайдите внутрь контейнера через консоль Bash:
```
docker exec -it <ID_контейнера> bash
```
8. Выполинте последовательно миграции и создание суперпользователя:
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
9. Наполнить БД тестовыми данными выполнив команду:
```sh
python manage.py dbfill
```
10. Проверьте доступность сервиса
```sh
http://localhost/admin
```  
## :books: Переменные среды
Этот образ использует переменные среды для настройки. Добавьте файл .env в папку infra и заполните переменные необходимыми значениями.

|Переменные              |Значение Default               |Описание                                            |
|------------------------|-------------------------------|----------------------------------------------------|
|`DB_ENGINE`             |`django.db.backends.postgresql`|Указываем движок БД                                 |
|`DB_NAME`               |`postgres`                     |Имя базы данных                                     |
|`POSTGRES_USER`         |no default                     |Логин дляподключения к БД                           |
|`POSTGRES_PASSWORD`     |no default                     |Пароль для подключения к БД                         |
|`DB_HOST`               |`db`                           |Название сервиса (контейнера)                       |
|`DB_PORT`               |5432                           |Порт для подключения к БД                           |
  
 ## ip-адрес сервера, на котором запущено приложение
 `51.250.111.148`
## :bust_in_silhouette: Автор проекта 
### :small_orange_diamond: Светлана  Петрова _(Svetlana Yu. Petrova)_
```html
e-mail: master-cim@yandex.ru
```
```html
https://github.com/master-cim
```
![Svetlana Yu. Petrova](https://sun9-5.userapi.com/impg/G-KmUqYd8SKbVr7jeVzeIlRh8lsbTmaSUTaHBw/CE-98blOBCo.jpg?size=500x501&quality=95&sign=74d83ffa8576a68a468dbbc9d4758dd1&type=album "Svetlana Yu. Petrova")
