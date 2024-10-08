from django import forms
from django.core.exceptions import ValidationError
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
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'نام کاربری باید با زبان انگلیسی و اعداد باشد')
    username = forms.CharField(validators=[alphanumeric], max_length=20,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'id': 'username',
                                          'placeholder': 'لطفا را نام کاربری خود را وارد کنید ...',
                                          'pattern': '^[0-9a-zA-Z]*$'
                                          }))

    class Meta:
        model = User
        fields = ['avatar', 'phone', 'username', 'first_name', 'last_name', 'email']
        widgets = {
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
                                          'placeholder': 'لطفا را نام کاربری خود را وارد کنید ...',
                                          'pattern': '^[0-9a-zA-Z]*$'
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


class UserChangePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'placeholder': 'رمز فعلی خود را وارد کنید ...'
               }
    ))
    new_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'placeholder': 'رمز جدید خود را وارد کنید ...'
               }
    ))
    conform_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'placeholder': 'دوباره رمز جدید خود را وارد کنید ...'
               }
    ))

    def clean_conform_password(self):
        password = self.cleaned_data.get('new_password')
        conform_password = self.cleaned_data.get('conform_password')
        if password == conform_password:
            return conform_password
        else:
            raise ValidationError('کلمه عبور و تکرار ان غیر هم سان هستند')


class UserChangePasswordResetForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control alert shadow',
               'placeholder': 'رمز جدید خود را وارد کنید ...'
               }
    ))
    conform_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control alert shadow',
               'placeholder': 'دوباره رمز جدید خود را وارد کنید ...'
               }
    ))

    def clean_conform_password(self):
        password = self.cleaned_data.get('new_password')
        conform_password = self.cleaned_data.get('conform_password')
        if password == conform_password:
            return conform_password
        else:
            raise ValidationError('کلمه عبور و تکرار ان غیر هم سان هستند')
