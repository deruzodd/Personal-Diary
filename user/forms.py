from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import UserModel, UserThemes, FontSizes


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password1', 'password2', 'theme')
    # email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
    #     'class': 'input',
    #     'placeholder': '',
    #     'required': 'True',
    # }))
    username = forms.CharField(
        label='Username', min_length=4, max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'required': 'true',
    }))
    password1 = forms.CharField(label='Password', min_length=5, max_length=20,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'required': 'True',
    }))
    password2 = forms.CharField(label='Repeat password', min_length=5, max_length=20,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'required': 'True',
    }))
    theme = forms.ChoiceField(label='Theme', choices=UserThemes.choices,
        widget=forms.Select(attrs={
            'class': 'form-select',
    }))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        # Check to see if any users already exist with this name as a username.
        try:
            match = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            # Check if username is not the Demo user's username
            if username != 'Guest':
                return username

        raise forms.ValidationError('This username is already in use.')


class LoginForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password')

class UserConfigForm(forms.Form):
    theme = forms.ChoiceField(
        label='Theme',
        choices=UserThemes.choices,
        widget=forms.Select(attrs={'class': 'form-select bg-basic bg-select'})
    )
    font_size = forms.ChoiceField(
        label='Font size',
        choices=FontSizes.choices,
        widget=forms.Select(attrs={'class': 'form-select bg-basic bg-select'})
    )
