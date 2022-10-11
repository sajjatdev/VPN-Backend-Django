
from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from .models import ServerJson, Membership, Customer, Transaction, Server, Payload
from Loginapp.models import User


class UserPasswordChaneg(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordChaneg, self).__init__(*args, **kwargs)


class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = ['name',  'Server_Host', 'Server_Port',
                  'SSL_Port', 'UDP_port',  'Flag']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'Server_Host': forms.TextInput(attrs={'class': 'form-control', }),
            'Server_Port': forms.TextInput(attrs={'class': 'form-control', }),
            'SSL_Port': forms.TextInput(attrs={'class': 'form-control', }),
            'UDP_port': forms.TextInput(attrs={'class': 'form-control', }),
        }


class PayloadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PayloadForm, self).__init__(*args, **kwargs)
        self.fields['SSL'].initial = "None"
        self.fields['SSL'].help_text = ' If you want to SSL please add value otherwise this field None'

    class Meta:
        model = Payload
        fields = ['name', 'payload', 'SSL',
                  'proxyIP', 'proxyport']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'payload': forms.Textarea(attrs={'class': 'form-control', }),
            'SSL': forms.TextInput(attrs={'class': 'form-control', }),
            'proxyIP': forms.TextInput(attrs={'class': 'form-control', }),
            'proxyport': forms.TextInput(attrs={'class': 'form-control', }),
        }


class ServerJsonForm(forms.ModelForm):
    class Meta:
        model = ServerJson
        fields = ['name', 'server', 'payload', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'server': forms.SelectMultiple(attrs={'class': 'form-control', }),
            'payload': forms.SelectMultiple(attrs={'class': 'form-control', }),
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
