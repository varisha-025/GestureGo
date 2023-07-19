
from django import forms
from django.contrib.auth.models import User 
class UserRegisterForm(forms.ModelForm):

    class Meta:
        model=User
        fields="__all__"
        
