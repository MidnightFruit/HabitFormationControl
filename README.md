# HabitFormationControl
Приложение по формированию привычек. Позволяет выработать привычку путём добавления её и напоминанием о ней с определённым интервалом (от _1_ до _7_ дней).

Проект запускается с помощью докера командой:

'docker-compose up -d --build'

В файле [docker-compose.yaml](https://github.com/MidnightFruit/HabitFormationControl/blob/c8f36977f5e041d998d6f93c25f0f1e1291a3fa4/docker-compose.yaml) прописаны настройки для контейнеров.

Для корректной работы требуется установить следующие переменные окружения в файле ".env". В таблице перечислены все требуемые переменные окружения.

|  Название переменной  |                       Описание переменной                        |
|:---------------------:|:----------------------------------------------------------------:|
|         DEBUG         |           Будет ли программа работать в дебаг режиме.            |
|      SECRET_KEY       |                      Секретный ключ Django.                      |
|      POSTGRES_DB      |                      Название базы данных.                       |
|     POSTGRES_USER     |                   Имя пользователя в Postgres.                   |
|   POSTGRES_PASSWORD   |                 Пароль пользователя в Postgres.                  |
|     POSTGRES_HOST     |                   Хост базы данных в Postgres.                   |
|     POSTGRES_PORT     |                          Порт Postgres.                          |
|    ALLOWED_ORIGINS    |                        Разрешенные хосты.                        |
|    TRUSTED_ORIGINS    |         Доверенные "источники" для безопасных запросов.          |
|   TELEGRAM_BOT_API    |                   HTTP API для Telegram бота.                    |
|   CELERY_BROKER_URL   |   URL для брокера Celery, в данном случае используется Redis.    |
| CELERY_RESULT_BACKEND | Хранилище выполненных задач, в данном случае используется Redis. |


