from django import forms

from .models import User


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(
                attrs={'class': 'form-control',
                       'id': 'password'}
            ),
            'username': forms.TextInput(
                attrs={'class': 'form-control',
                       'id': 'username'}
            ),
        }
