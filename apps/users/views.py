from django.shortcuts import render
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model
from apps.users.serializers import UserSerializers
from rest_framework.permissions import IsAuthenticated


User = get_user_model()


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = []
    serializer_class = UserSerializers

class UpdateUserView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsAuthenticated,)

class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsAuthenticated,)

class DeleteUserView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsAuthenticated,)