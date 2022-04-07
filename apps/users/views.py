from django.shortcuts import render
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model
from apps.users.serializers import UserSerializer


User = get_user_model()


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    #permission_classes = [permissions.AllowAny] # Or anon users can't register]
    serializer_class = UserSerializer

class UpdateUserView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DeleteUserView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer