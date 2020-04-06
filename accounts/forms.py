from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'  

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']  
        widgets={
            'username':forms.TextInput(attrs={'class':'form__input','placeholder':'Username'}),
            'email':forms.EmailInput(attrs={'class':'form__input','placeholder':'Email','id':'email'}),
             }


