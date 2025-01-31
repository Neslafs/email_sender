from rest_framework import serializers

from .models import Mail


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = ['to', 'subject', 'body', 'mail_attachment']