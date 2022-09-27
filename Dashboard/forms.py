
from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from .models import update, Membership, Customer, Transaction
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
        fields = ['id', 'title', 'duration', 'name']
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'autocomplete': 'off'}),
            'name': forms.Select(attrs={'class': 'form-control', 'required': 'required', 'autocomplete': 'off'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'required': 'required', 'autocomplete': 'off'}),

        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "username", 'password', 'membership']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'autocomplete': 'off'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'autocomplete': 'off'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'required': 'required', 'autocomplete': 'new-password'}),
            'membership': forms.Select(attrs={'class': 'form-control', 'required': 'required', 'autocomplete': 'off'}),
        }
