from django.core.mail import EmailMessage
from django.conf import settings


MAX_FILE_SIZE = settings.MAX_UPLOAD_SIZE

def send_email(to,subject,body,from_email,files):

    email = EmailMessage(
                to=to,
                subject = subject,
                body = body,
                from_email = from_email,
            )
    if files:
        for file in files:
            if file.size > MAX_FILE_SIZE:
                return {'status': 'error', 'message': f'Файл {file.name} превышает 10 МБ'}
            email.attach(file.name, file.read(), file.content_type)
    try:
        email.send()
        return {'status': 'success', 'message': 'Ты успешно доставил почту'}
    except Exception as e:
        return {'status': 'error', 'message': f'При отправлении произошла ошибка {e}'}


