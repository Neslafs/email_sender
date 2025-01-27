# Email Sender
Email Sender — это простое Django-приложение для отправки электронных писем через веб-интерфейс и REST API. Проект поддерживает авторизацию пользователей, историю отправленных писем и прикрепление файлов.
Работет на базе данных PostgreSQL.
На данный момент в проекте присутствует: 
- Авторизация пользователей через форму и сессии.
- Отправка писем через веб-интерфейс с возможностью прикрепления файлов.
- REST API для работы с письмами.
- История отправленных писем.

# Установка 

На данный момент залил проект чисто для ознакомления с кодом.

1. Клонируйте репозиторий: https://github.com/Neslafs/email_sender.git

2. Перейдите в папку проекта: cd email-sender

3. Установите зависимости: pip install -r requirements.txt

4. Установите PostegreSQL: https://www.postgresql.org/download/

5. Создайте базу данных PostegreSQL, после чего подключите БД в настройках проекта.
Используйте файл settings_example как шаблон настроек (в настройках также требуется ввести данные вашей почты: https://help.mail.ru/mail/mailer/2fa/).

7. Выполните миграции: python manage.py migrate

8. Запустите сервер разработки: python manage.py runserver

# Использование

Через графический интерфейс: 

1. Войдите в систему через веб-интерфейс: http://127.0.0.1:8000/login

2. Отправьте письмо через веб-форму: http://127.0.0.1:8000/send-email

3. Просмотрите историю отправленных писем: http://127.0.0.1:8000/email_history

Через API:

Для работы с API на данный момент требуется авторизация через графический интерфейс: http://127.0.0.1:8000/login

После успешной авторизации вы можете использовать следующие эндпоинты:

- Получения списка писем:
GET /api/mails/

- Создание письма
POST /api/mails/

Пример:

  {

      "to": "example@example.com",

      "subject": "Test email",

      "body": "This is a test",

      "mail_attachment": null

  }

# Что будет реализовано / в прогрессе
- Сессионая аутентификация будет заменена на токены
- Возможность массовой рассылки писем
- Возможность рассылки HTML-шаблонов для тела письма
- Фильтрация в истории
- Асинхронная отправка писем с помощью Celery
- Улучшение безопасности
