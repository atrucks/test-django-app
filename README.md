# Приложение для тестовой задачи администрирования

Для своей работы требует PostgreSQL и Redis.

Также для запуска ему должны быть заданы следующие переменные окружения:

- `SECRET_KEY` - секретный ключ
- `DEBUG` - `0` или `1`
- `HOST` - имя хоста (домена), с которого разрешено делать запросы  
Подробнее смотри в [документации](https://docs.djangoproject.com/en/stable/ref/settings/#allowed-hosts).
- `POSTGRES_HOST` - адрес сервера PostgreSQL
- `POSTGRES_DB` - имя базы данных приложения (её нужно будет создать)
- `POSTGRES_USER` - имя пользователя базы данных
- `POSTGRES_PASSWORD` - пароль пользователя
- `REDIS_ADDR` - адрес сервера Redis
