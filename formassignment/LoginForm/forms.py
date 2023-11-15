from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

def validate_password_contains_uppercase(value):
    if not any(char.isupper() for char in value):
        raise ValidationError("The password must contain at least one uppercase letter.")
    
class LoginForm(forms.Form):
    userName = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, validators = [validators.MinLengthValidator(8), validate_password_contains_uppercase])