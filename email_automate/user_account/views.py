from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_302_FOUND

from .serializers import UserSerializers

# Create your views here.

@login_required
def user_logout(request):
    try:
        logout(request)
        return redirect('login')
    except Exception as e:
        return HttpResponse(f"<h2>Error : {str(e)} </h2>", status=500)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return Response({'detail': 'Creating new users is not allowed.'}, status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        # если пользователь не администратор, то перенаправляет на его страницу
        if not self.request.user.is_staff:
            user_url = reverse('user-detail', args=[request.user.id])
            return Response(
                {"detail": "Redirecting to your profile."},
                status=HTTP_302_FOUND,
                headers={'Location': user_url}  # Указываем URL для редиректа в заголовке
            )
        # если администратор, то позволяет увидеть список всех пользователей
        return super().list(request, *args, **kwargs)


