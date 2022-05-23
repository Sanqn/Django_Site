from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms


class SigUpForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        label='Username',
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control mt-2",
            'id': "inputUsername",
            'placeholder': "Input username",

        }),
    )

    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "inputPassword",
            'placeholder': "Input password",
        }),
    )
    repeat_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "ReInputPassword",
            'placeholder': "Repeat password",
        }),
    )

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['repeat_password']

        if password != confirm_password:
            raise forms.ValidationError(
                "Passwords do not match"
            )

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        user.save()
        auth = authenticate(**self.cleaned_data)
        return auth


class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        label='Username',
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control mt-2",
            'id': "inputUsername",
        }),
    )

    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "inputPassword",
        }),
    )