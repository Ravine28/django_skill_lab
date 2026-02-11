from django import forms
from .models import Access, Client, System
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class SystemForm(forms.ModelForm):
    class Meta:
        model = System
        fields = '__all__'


class AccessForm(forms.ModelForm):
    class Meta:
        model = Access
        fields = '__all__'


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']