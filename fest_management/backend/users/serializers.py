from rest_framework import serializers
from .models import CustomUser  # Ensure CustomUser is imported

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number']
