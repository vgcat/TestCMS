from django.forms import ModelForm
from django.contrib.auth.hashers import make_password
from cms.models import User

class RegisterForm(ModelForm):
    class Meta:
        model = User    
        fields = ('email', 'password' ,'first_name', 'last_name', 'avatar')
    def clean_password(self):
        password = self.cleaned_data['password']
        return make_password(password)
