from django import forms
from django.core.exceptions import ValidationError

def validate_pass_length(value):
    if len(value) < 8:
        raise ValidationError("Password must be 8 characters in length.")
def validate_empty(value):
    if not value:
        raise ValidationError("This field is required.")

class UserRegistration(forms.Form):
    """
    Define the user and organization registration fields.
    """
    first_name = forms.CharField(validators=[validate_empty],label='First Name', max_length=18, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email Address', max_length=64, widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    org_name = forms.CharField(label='Organization Name', max_length=32, widget=forms.TextInput(attrs={'class':'form-control'}))
    website = forms.URLField(label='Website', widget=forms.URLInput(attrs={'class':'form-control'}))
    logo = forms.ImageField(label='Organization Logo', required=False, widget=forms.FileInput(attrs={'class':'form-control'}))
    contact = forms.EmailField(label='Contact Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password', 'org_name', 'website', 'logo', 'contact', 'description']


class LoginForm(forms.Form):
    """
    Define the Login fields.
    """
    email = forms.EmailField(label='Email Address')
    password = forms.PasswordInput()

