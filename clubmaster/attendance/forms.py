from django import forms

class MemberCreationForm(forms.Form):
    """
        Form for creating a new member of an organization
    """
    first_name = forms.CharField(label='First Name', max_length=18, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email Address', max_length=64, widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone_num = forms.IntegerField(label='Phone Number', widget=forms.NumberInput(attrs={'class':'form-control'}))
    college = forms.CharField(label='College', max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    grad_year = forms.IntegerField(label='Grad Year', widget=forms.NumberInput(attrs={'class':'form-control'}))
