from rest_framework import serializers
from cms.models import User
from django.contrib.auth.hashers import make_password
 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password' ,'first_name', 'last_name', 'date_joined','is_active', 'avatar', 'is_staff')
    def validate_password(self, value):
        return make_password(value)
    