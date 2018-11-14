from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from cms.models import User
# Create your views here.

class RegisterUser(APIView):
    

    def post(self, data=r):
        """
        Have to create user
        """
        
        user = User.objects.create_user()
        return user