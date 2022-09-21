

from dataclasses import fields
from django import forms
from .models import update
from Loginapp.models import User


class UpdateForm(forms.ModelForm):
    class Meta:
        model = update
        fields = ['name', 'jsondata', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'jsondata': forms.Textarea(attrs={'class': 'form-control', }),

        }


class ReSellerForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password',
                  'first_name', 'last_name', 'is_admin', 'credit')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', }),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', }),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', }),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'required', }),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'required': 'required', }),
        }
