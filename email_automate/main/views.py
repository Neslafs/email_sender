from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

from .utils import send_email
from .forms import MailForm
from .models import Mail
from .serializers import MailSerializer



def main_page(request):
    return render(request, 'main/main_page.html')

@login_required
def email_history(request):
    emails = Mail.objects.all()
    return render(request, 'main/email_history.html', {'emails': emails})

@login_required
def email_history_info(request, pk):
    emails = Mail.objects.get(pk = pk)
    return render(request, 'main/email_history_info.html', {'emails': emails})

@login_required
def create_email(request):
    if request.method == "POST":
        email_form = MailForm(request.POST, request.FILES)

        if email_form.is_valid():
            email_instance = email_form.save(commit=False)
            email_instance.from_user = request.user

            result = send_email(
                to=[email_form.cleaned_data['to']],
                subject=email_form.cleaned_data['subject'],
                body=email_form.cleaned_data['body'],
                from_email = settings.EMAIL_HOST_USER,
                files=request.FILES.getlist('mail_attachment') if 'mail_attachment' in request.FILES else []

           )

            if result['status'] == 'sucсess':
                email_instance.save()
                return HttpResponse("<h2>You deliver the email!</h2>")

            else:
                return HttpResponse(f"<h2>Error: {result['message']}</h2>")

    else:
        email_form = MailForm()
    return render(request, 'main/send_email.html', {"email_form": email_form})

# API

class MailViewSet(viewsets.ModelViewSet):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
    permission_classes = [IsAuthenticated]

    # Фильтрация
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('to', 'sent_date')

    def get_queryset(self):
        # Фильтруем письма по текущему пользователю
        return Mail.objects.filter(from_user=self.request.user)


