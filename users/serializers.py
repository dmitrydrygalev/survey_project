from rest_framework import serializers
from .models import *


class RegistrationSerializer(serializers.ModelSerializer):
    repeat_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'repeat_password']

    def save(self, *args, **kwargs):
        user = CustomUser(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        repeat_password = self.validated_data['repeat_password']
        if password != repeat_password:
            raise serializers.ValidationError("[WARNING] Введеные пароли не совпадают!")
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
