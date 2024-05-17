import re
from django import forms
from .models import CustomUser

from django.contrib.auth.hashers import make_password


class RegistrationForm(forms.ModelForm):
    """
    It is used to Register New Users,
        - It validate password and encrypt it before storing it into database
        - It validate mobile, which can be any valid Indian mobile number
    """
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'mobile', 'city', 'password',
                  'gender', 'role', ]

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,}$', password):
            raise forms.ValidationError(
                "Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one number, and one special character (!@#$%^&*).")
        return make_password(password)

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not re.match(r'^\+?91?\d{9,10}$', mobile):
            raise forms.ValidationError("Mobile number must be an Indian number.")
        return mobile


class LoginForm(forms.Form):
    """
    It is used to log in user
    """
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
