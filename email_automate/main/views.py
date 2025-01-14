from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.core.mail import EmailMessage
from django.template.context_processors import request

from .forms import MailForm
from .models import Mail

def send_email(request):
    email = EmailMessage(
        subject = 'Tech Support',
        body = 'We received your request for tech service. We are working on it.',
        from_email= 'pelicanpelican@mail.ru',
        to = ['nessem17@mail.ru'],
    )
    #email.send()
    return HttpResponse("<h2>You deliver the email!</h2>")

def send_email_view(mail_subject, mail_message, user_email, personal_mail):
    email = EmailMessage (
        subject=mail_subject,
        body = mail_message,
        from_email='pelicanpelican@mail.ru',
        to = user_email,
        headers={'Reply-To' : personal_mail}
    )
    email.send()

def email_sender(request):
    if request.method == "POST":
        mail_form = EmailForm(request.POST)
        if mail_form.is_valid():
            email = EmailMessage(
                subject = mail_form.cleaned_data['subject'],
                body = mail_form.cleaned_data['message'],
                reply_to = [mail_form.cleaned_data['reply_to']],
                from_email = 'pelicanpelican@mail.ru',
                to = ['lolka1158@gmail.com'],
            )
            email.send()
            return HttpResponse("<h2>You deliver the email!</h2>")
    else:
        mail_form = EmailForm()
    return render(request, 'main/send_email.html', {"mail_form":mail_form})

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



