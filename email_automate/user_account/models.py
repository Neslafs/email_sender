from django.db import models

# Create your models here.

class UserProfile (models.Model):
    first_name = models.CharField('Имя пользователя', max_length=50)
    last_name = models.CharField('Фамилия пользователя', max_length=50)
    profile_name = models.CharField('Логин пользователя', max_length=50)
    user_email = models.EmailField('Почта пользователя', max_length=250 )
    creation_date = models.DateField('Дата создания пользователя')

class Subscriber(models.Model):
    subscribed_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)



