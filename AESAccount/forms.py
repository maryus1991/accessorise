from django import forms
from django.core.validators import RegexValidator

from .models import User


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(
                attrs={'class': 'form-control',
                       'id': 'password',
                       'placeholder': 'لطفا رمز عبور خود را وارد کنید ...'
                       }
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control',
                       'id': 'username',
                       'placeholder': 'لطفا را ایمیل خود را وارد کنید ...'
                       },

            ),
        }


class UserRegisterForm(forms.ModelForm):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'نام کاربری باید با زبان انگلیسی و اعداد باشد')
    username = forms.CharField(validators=[alphanumeric], max_length=20,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'id': 'username',
                                          'placeholder': 'لطفا را نام کاربری خود را وارد کنید ...'
                                          }))

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(
                attrs={'class': 'form-control',
                       'id': 'password',
                       'placeholder': 'لطفا رمز عبور خود را وارد کنید ...'
                       }
            ),
            'username': forms.TextInput(
                attrs={'class': 'form-control',
                       'id': 'username',
                       'placeholder': 'لطفا را نام کاربری خود را با اعداد و حروف انگلیسی وارد کنید ...'
                       },

            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control',
                       'id': 'username',
                       'placeholder': 'لطفا را نام ایمیل خود را وارد کنید ...'
                       },

            ),
        }
