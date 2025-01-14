from django import forms
from django.db.models import Model
from django.forms import ModelForm
from .models import Mail

class EmailForm(forms.Form):
    subject = forms.CharField(
                                label='Тема', max_length=300,
                                widget= forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder' : 'Тема письма'
                                })
                              )

    message = forms.CharField(
                                label='Сообщение',
                                widget = forms.Textarea(attrs={
                                'class': 'form-control',
                                'placeholder' : 'Текст сообщения'
                                })
                            )

    reply_to = forms.EmailField(label='Ответ можно прислать сюда:', max_length=300,
                                widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder' : 'Ответ можно прислать сюда:'
                                })
                            )

class MailForm(ModelForm):
    class Meta:
        model = Mail
        fields = ['to','subject','body', 'mail_attachment']



        widgets = {
            'to' : forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder' : 'Получатель'
        }),
            'subject' : forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder' : 'Тема сообщения'
        }),
            'body' : forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Текст сообщения'
        }),
            'mail_attachment' : forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'placeholder' : 'Прикрепить файл'
            }),
    }
