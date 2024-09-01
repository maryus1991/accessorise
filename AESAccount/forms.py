from django import forms
from django.core.validators import RegexValidator

from .models import User


class EditAddrForm(forms.Form):
    addr = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'ادرس خود را وارد کنید',
        'name': 'addr',
    }))

    post = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'کد پستی خود را وارد کنید',
        'name': 'post',
    }))


class UserEditProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'phone', 'username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'نام کاربری (حتما باید انگلیسی باشد)',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام خانوادگی',
            }),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ایمیل',
                }),
            'avatar': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'عکس پروفایل',
                }),
            'phone': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'شماره تماس',
                }),
        }

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        avatar.name = str(avatar.name).replace(' ', 'xx')
        return avatar


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
