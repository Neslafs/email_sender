from rest_framework.test import APITestCase
from rest_framework import status
from .models import Mail


class MailAPITestCase(APITestCase):
    def setUp(self):
        self.mail_data = {
            "to": "",
            "subject": "Проверка проверка",
            "body": "Проверка текст"
        }
        self.response = self.client.post('/api/mails/', self.mail_data, format='json')

    def test_create_mail(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_mail_list(self):
        response = self.client.get('/api/mails/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)