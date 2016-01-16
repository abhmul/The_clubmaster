from django import forms


class UserRegistration(forms.Form):
    """
    Define the user registration fields.
    """
    first_name = forms.CharField(label='First Name', max=18)
    last_name = forms.CharField(label='Last Name', max_length=30)
    email = forms.EmailField(label='Email Address', max_length=64)
    password = forms.PasswordInput()

    fields = ['first_name', 'last_name', 'email', 'password']


class OrganizationRegistration(forms.Form):
    """
    Define the Organization registration fields.
    """
    org_name = forms.CharField(label='Organization Name', max_length=32)
    website = forms.URLField(label='Website')
    logo = forms.ImageField(label='Organization Logo', required=False)
    contact = forms.EmailField(label='Contact Email')
    description = forms.Textarea()

    fields = ['org_name', 'website', 'logo', 'contact', 'description']
