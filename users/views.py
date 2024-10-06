from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from tutorial.quickstart.serializers import UserSerializer

from users.models import User


class UserCreateAPIview(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [~IsAuthenticated]