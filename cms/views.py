from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from cms.models import User
# Create your views here.

class RegisterUser(APIView):
    

    def post(self, request):
        """
        Have to create user
        """
        email = request. email
        password = request.password
        user = User.objects.create_user(email, password=password)
        return user