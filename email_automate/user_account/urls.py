from django.contrib import admin
from django.contrib.auth import views
from django.urls import path
from .views import user_logout


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('user_logout/', user_logout, name='custom_logout'),
    path('reset_password/', views.PasswordResetView.as_view(), name='reset_password'),
    path('password_reset_done', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]