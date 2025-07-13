from django import forms
from .models import ABC
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ABCForm(forms.ModelForm):
    class Meta: #The inner class Meta tells Django how to build the form from a model.
        model= ABC
        fields = ['text', 'photo']  # Specify the fields 
        
class UserRegistrationForm(UserCreationForm):
    email= forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # Specify the fields 