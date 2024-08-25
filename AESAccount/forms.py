from django import forms

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
                       }
            ),
        }


class UserRegisterForm(forms.ModelForm):
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
            # 'conform_password': forms.PasswordInput(
            #     attrs={'class': 'form-control',
            #            # 'id': 'password',
            #            'placeholder': 'لطفا رمز عبور خود را تایید کنید ...'
            #            }
            # ),
            'username': forms.TextInput(
                attrs={'class': 'form-control',
                       'id': 'username',
                       'placeholder': 'لطفا را نام کاربری خود را وارد کنید ...'
                       }
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control',
                       'id': 'username',
                       'placeholder': 'لطفا را نام ایمیل خود را وارد کنید ...'
                       }
            ),
        }
