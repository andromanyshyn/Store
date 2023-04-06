from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from .models import User
from .tasks import send_email_verification


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Surname',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Username',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Email',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Repeat Password',
    }))

    def save(self, commit=True):
        user = super().save(commit=True)
        send_email_verification.delay(user.id)
        return user

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',
                  'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Username'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Password'
    }))

    class Meta:
        model = User
        fields = ['username', 'password']


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input', 'placeholder': 'Choose the image'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'readonly': True}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'readonly': True}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'image',
                  'username', 'email', ]
