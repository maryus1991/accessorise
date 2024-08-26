from django import forms

from .models import Contact_us


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact_us
        fields = ('full_name', 'email', 'subject', 'message', 'phone')
        widgets = {
            'full_name': forms.TextInput(attrs={'id': 'validationDefault01',
                                                'placeholder': 'نام و نام خانوادگی'}),
            'phone': forms.NumberInput(attrs={'id': 'validationDefault02',
                                              'placeholder': 'شماره همراه'}),
            'email': forms.EmailInput(attrs={'id': 'validationDefault03',
                                             'placeholder': 'ایمیل'}),
            'subject': forms.TextInput(attrs={'id': 'validationDefault04',
                                              'placeholder': 'موضوع'}),
            'message': forms.Textarea(attrs={'id': 'validationDefault05',
                                             'placeholder': 'پیام ...',
                                             'cols': "30", 'rows': "10"}),
        }
