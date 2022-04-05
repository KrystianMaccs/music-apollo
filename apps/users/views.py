from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from apps.users.serializers import UserSerializer, CreateUserSerializer


User = get_user_model()


class CreateUserView(generics.CreateAPIView):
    model = User
    #permission_classes = [permissions.AllowAny # Or anon users can't register]
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