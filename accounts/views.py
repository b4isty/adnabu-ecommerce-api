from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer

User = get_user_model()


class RegisterView(CreateAPIView):
    """
    Class for Register
    """
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny, ]
    queryset = User.objects.all()


