from dataclasses import field
from pyexpat import model
from tkinter.tix import Form
from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from .models import update, Membership
from Loginapp.models import User


class UserPasswordChaneg(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordChaneg, self).__init__(*args, **kwargs)


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


class MembershipForm(forms.ModelForm):

    class Meta:
        model = Membership
        fields = ['duration', 'name']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control', 'required': 'required', 'autocomplete': 'off'}),
            'duration': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'autocomplete': 'off'}),

        }
