from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.core.mail import EmailMessage
from django.template.context_processors import request
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

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

            email = EmailMessage(
                to=[email_form.cleaned_data ['to']],
                subject = email_form.cleaned_data['subject'],
                body = email_form.cleaned_data['body'],
                reply_to = ['pelicanpelican@mail.ru'],
                from_email = 'pelicanpelican@mail.ru',
            )
            email_instance.from_user = request.user

            if 'mail_attachment' in request.FILES:
                for mail_attachment in request.FILES.getlist('mail_attachment'):
                    email.attach(mail_attachment.name, mail_attachment.read(), mail_attachment.content_type)
            try:
                email.send()
                email_instance.save()
                return HttpResponse("<h2>You deliver the email!</h2>")

            except Exception as e:
                return HttpResponse(f"<h2>Error : {e} </h2>")
    else:
        email_form = MailForm()
    return render(request, 'main/send_email.html', {"email_form": email_form})

# API

class MailViewSet(viewsets.ModelViewSet):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
    permission_classes = [IsAuthenticated]

