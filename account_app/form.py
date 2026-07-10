from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'مثل: علی احمدی'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'*********'}),)


    def clean_password(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            return self.cleaned_data['password']
        else:
            raise ValidationError("رمز یا نام کاربری صحیح نیست", "1005")


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام کاربری جدیدی برای خود انتخاب کنید.'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '*********'}),)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '*********'}),)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("این نام کاربری از قبل وجود دارد", "1007")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("رمز ها همخوانی ندارند", code="1006")

        return cleaned_data

