from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm,UserChangeForm
from django import forms

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'

class EditUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']