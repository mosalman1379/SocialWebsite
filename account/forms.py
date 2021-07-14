from django import forms
from django.contrib.auth.models import User
from account.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    """
    User form registration
    """
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirmPassword = forms.CharField(widget=forms.PasswordInput, label='Password')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_confirmPassword(self):
        clean = self.cleaned_data
        if clean['password'] != clean['confirmPassword']:
            raise forms.ValidationError('Password don\' match')
        return clean['password']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('data_of_birth', 'photo')
