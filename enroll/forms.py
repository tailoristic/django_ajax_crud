from django import forms
from django import forms
from django.forms import widgets
from .models import UserModel


class UserRegistration(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['name','email','password']
        widgets = {
            'name' : forms.TextInput(
                attrs={
                 'class':'form-control',    
                 'id':'nameid',
                }),
            'email' : forms.EmailInput(
                attrs={
                 'class':'form-control',   
                 'id':'emailid',
                }),
            'password' : forms.PasswordInput(
                attrs={
                 'class':'form-control',   
                 'id':'passwordid',
                })
        }
        