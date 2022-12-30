from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from .models import CustomUser
from .serializers import RegistrationSerializer, LoginSerializer
from django.contrib.auth import authenticate


class RegistrationUserView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        serializer = RegistrationSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class AuthorizationUserView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid()

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        try:
            user = CustomUser.objects.get(email=email)
        except:
            raise ValidationError({"[Not Found]": 'Аккаунт не найден!'})
        check_user = authenticate(username=email, password=password, request=request)
        if check_user is not None:
            return Response({'Пользователь': user.email}, status=status.HTTP_200_OK)
        else:
            raise ValidationError({"[Not Found]": 'Аутентификация не пройдена!'})
