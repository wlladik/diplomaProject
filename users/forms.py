from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegForm(UserCreationForm):
    email = forms.EmailField(
        label='Your email:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your email'})
    )

    username = forms.CharField(
        label='Your username:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your username'})
    )

    password1 = forms.CharField(
        label='Your password:',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    password2 = forms.CharField(
        label='Confirm your password:',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class UserUpdateForm(forms.ModelForm):
        email = forms.EmailField(
            label='Your email:',
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your email'})
        )

        username = forms.CharField(
            label='Your username:',
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your username'})
        )

        class Meta:
            model = User
            fields = ['username', 'email']

class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Upload picture:',
        required=False,
        widget=forms.FileInput
    )
    class Meta:
        model = Profile
        fields = ['img']

class SexForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['sex']

class BoolForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['my_bool']
