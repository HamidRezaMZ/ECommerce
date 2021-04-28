from django import forms
from django.core import validators


class CreateContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'لطفا نام نام خانوادگی خود را وارد نمایید', 'class': "form-control"}),
        label='نام و نام خانوادگی',
        validators=[
            validators.MaxLengthValidator(150, 'تعداد کاراکترهای وارد شده نمیتواند بیشتر از 150 باشد')
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید', 'class': "form-control"}),
        label='ایمیل',
        validators=[
            validators.MaxLengthValidator(150, 'ایمیل وارد شده نمی تواند بیشتر از 150 کاراکتر باشد.')
        ]
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا عنوان خود را وارد نمایید', 'class': "form-control"}),
        label='موضوع',
        validators=[
            validators.MaxLengthValidator(200, 'عنوان پیام نمی تواند بیشتر از 200 کاراکتر باشد.')
        ]
    )

    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'لطفا متن خود را وارد نمایید', 'class': "form-control", "rows": 8}),
        label='متن پیام'
    )
