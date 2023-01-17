from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields=['first_name','last_name','username','email','password1','password2']


class AddSecretaryForm(UserCreationForm):
    class Meta:
        model = User
        fields=['first_name','last_name','username','email','password1','password2','role']


class AddScheduleForm(ModelForm):
    class Meta:
        model = ScheduleModel
        fields = ['Reciever','username','subject', 'message']


