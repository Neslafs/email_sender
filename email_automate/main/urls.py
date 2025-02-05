from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

from .views import MailViewSet

router = DefaultRouter()
router.register(r'api/mails', MailViewSet, basename='mail')

urlpatterns = [
    path('create_email', views.create_email, name='create_email'),
    path('accounts/', include('user_account.urls')),
    path('email_history', views.email_history, name='email_history'),
    path('email_history/<int:pk>', views.email_history_info, name='email_history_info'),
    path('',views.main_page, name='main_page'),
]

urlpatterns += router.urls