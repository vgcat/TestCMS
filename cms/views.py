from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView)
from django.contrib.auth.hashers import make_password

#from rest_framework import authentication, permissions, status
#from rest_framework.parsers import JSONParser
#from rest_framework.renderers import JSONRenderer
#from rest_framework.response import Response
#from rest_framework.views import APIView

from cms.models import (TournamentPost, User)
from cms.forms import RegisterForm
#from cms.serializers import UserSerializer
# Create your views here.

class RegisterUserView(CreateView):
    form_class = RegisterForm
    template_name = "registration/user_form.html"
    success_url = "/login/"
    
    def validate_password(self, value):
        return make_password(value)


class TournamentListView(ListView):
    model = TournamentPost
    template_name = "tournament_post_list.html"

class TournamentPostView(DetailView):
    model = TournamentPost
    template_name = "post_detail"
    pk_url_kwarg ='post_id'

class TournamentPostCreateView(CreateView):
    model = TournamentPost
    template_name = "tournament_post_form.html"
    fields = ('title', 'text', 'tags', 'game', 'delay_time')
    success_url = "/tournament/list/"


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
