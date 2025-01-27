from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'date_joined']
        read_only_fields = ['is_staff', 'date_joined']