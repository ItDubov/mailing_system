# Mailing System

Это система рассылок, разработанная с использованием Django, предназначенная для создания и отправки сообщений клиентам в определенные временные интервалы. В этой системе вы можете управлять клиентами, создавать сообщения и запускать рассылки.

## Установка и запуск

### 1. Клонирование репозитория

Клонируйте репозиторий с GitHub:

```bash
git clone https://github.com/yourusername/mailing-system.git
cd mailing-system
```

2. Установка зависимостей
Создайте виртуальное окружение и активируйте его:
python -m venv venv
Для Windows:
 venv\Scripts\activate
 pip install -r requirements.txt
3. Настройка базы данных
Примените миграции для создания таблиц в базе данных:
python manage.py migrate
4.  Создание суперпользователя
Для доступа к админке Django создайте суперпользователя:
python manage.py createsuperuser
5. Запуск сервера
Запустите сервер разработки:
python manage.py runserver
Теперь приложение доступно по адресу: http://127.0.0.1:8000/.
6. Доступ к админке Django
Перейдите в админку по следующему URL: http://127.0.0.1:8000/admin/ и войдите с учетными данными суперпользователя.
Структура проекта
core: Основное приложение, которое содержит базовые страницы и представления.

mailing: Приложение для управления рассылками, сообщениями и клиентами.

models.py: Определение моделей для сообщений, рассылок и клиентов.

views.py: Логика представлений для управления рассылками.

admin.py: Регистрация моделей для работы с админкой Django.

clients: Приложение для управления клиентами, которые получают рассылки.

users: Приложение для работы с пользователями (включая суперпользователей).

Как использовать
Админка Django
Создание сообщения:

Перейдите в раздел Messages в админке и создайте новое сообщение с темой и текстом.

Создание клиента:

Перейдите в раздел Clients в админке и добавьте клиента, указав его имя и email.

Создание рассылки:

Перейдите в раздел Mailings в админке и создайте новую рассылку.

Выберите сообщение, которое будет отправлено, добавьте список клиентов, установите дату начала и окончания рассылки.

Запуск рассылки:

Для тестирования можно использовать Django shell или создать кастомную логику для автоматической отправки сообщений.

Отправка Email
Для настройки отправки email сообщений, откройте файл settings.py и добавьте параметры для почтового сервера. Например, для использования Gmail:

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_password'
Вы можете использовать функцию send_mail для отправки сообщений клиентам.

Пример отправки сообщений
Пример кода для отправки сообщений клиентам в рамках рассылки:
from mailing.models import Mailing
from django.core.mail import send_mail
from django.utils import timezone

# Получите все активные рассылки
active_mailings = Mailing.objects.filter(status='started', end_date__gte=timezone.now())

for mailing in active_mailings:
    # Отправка сообщений всем клиентам
    for client in mailing.clients.all():
        send_mail(
            mailing.message.subject,  # Тема
            mailing.message.body,  # Тело сообщения
            'from@example.com',  # От кого
            [client.email],  # Кому
            fail_silently=False,
        )
Важные файлы
settings.py: Здесь настраиваются параметры базы данных, почты и другие настройки проекта.

models.py: Определение моделей для базы данных.

views.py: Представления для работы с шаблонами и логикой рассылок.

admin.py: Настройка админки для управления моделями через интерфейс.


