from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms
from .models import Comment


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


class FeedBackForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Name',
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
            'placeholder': "Your name",
        }),
    )

    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': "form-control",
            'id': "Email",
            'placeholder': "Email"
        }),
    )

    subject = forms.CharField(
        max_length=250,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'subject',
            'placeholder': "Subject"
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control md-textarea',
            'id': 'message',
            'rows': 2,
            'placeholder': "Your message"
        })
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }
