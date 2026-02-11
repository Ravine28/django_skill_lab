from django import forms
from .models import Access, Client, System

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
