from django import forms
from users.models import MyUsers


class LoginForm(forms.Form):
    """
    2 Fields for log in.No connection with any model.
    """
    # username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Valid Email ID'}))
    email = forms.EmailField(required=True, label="Please enter your email address",
                             widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': ' Password'}))


class RegistrationForm(forms.ModelForm):
    """
    For accessing the inbuilt User model
    """
    email = forms.EmailField(required=True, label="Please enter your email address",
                             widget=forms.EmailInput(attrs={"class": "form-control",'placeholder': 'valid email'}))

    class Meta:
        model = MyUsers
        fields = ['email', 'first_name', 'last_name', 'password','phone_number']

        widgets = {
            # "username": forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'Valid Email ID'}),
            "first_name": forms.TextInput(
                attrs={"class": "form-control", 'placeholder': 'First Name', 'pattern': '[A-Z a-z]+',
                       'title': 'Enter Characters Only '}),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", 'placeholder': 'Last Name', 'pattern': '[A-Z a-z]+',
                       'title': 'Enter Characters Only '}),
            "password": forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'create password'}),
            "phone_number":forms.NumberInput(
                attrs={"class": "form-control", 'placeholder': 'Phone number', 'pattern': '[0-9]',
                       'title': 'Enter Numbers Only '}),

        }
