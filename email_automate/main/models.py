from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Mail(models.Model):
    to = models.EmailField('Получатель', max_length=300)
    subject = models.CharField('Тема', max_length=300)
    body = models.TextField('Сообщение')
    reply_to = models.EmailField('Ответ можно прислать сюда:', max_length=300, default = '')
    from_email = models.EmailField('От:', max_length=300, default = '')
    mail_attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None,
                                  null=True, blank=True)
    sent_date = models.DateField('Дата создания письма', default=now)

    def __str__(self):
        return self.subject