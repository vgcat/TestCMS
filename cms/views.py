#for serializing
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import authentication, permissions, status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from cms.models import User
from cms.serializers import UserSerializer
from django.views.generic import TemplateView, CreateView,UpdateView, DeleteView, DetailView


# Create your views here.

class RegisterUser(CreateView):
    model = User
    fields = ['email', 'password' ,'first_name', 'last_name', 'is_active', 'avatar', 'is_staff']
    template_name = "user_form.htlm"
    success_url = "login_form.html"

class LoginUser(CreateView):
    model = User
    fields=['email', 'password']
    def create_access(self):
        return a
    


#class RegisterUser(APIView):
#    model = User
#    serializer_class = UserSerializer
#
#    def post(self, request, *args, **kwargs):
#    
#        serializer = UserSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(
#                serializer.data, status=status.HTTP_201_CREATED)
#        else:
#            return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)
