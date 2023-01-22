from django import forms
from users.models import MyUsers

from .models import SellerModel


# buyer Form
class LoginForm(forms.Form):
    """
    2 Fields for log in.No connection with any model.
    """
    # username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Valid Email ID'}))
    email = forms.EmailField(required=True, label="Enter Your Email Address",
                             widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': ' Password'}))


# class DateInput(forms.DateInput):
#     input_type = 'date'


class RegistrationSellerForm(forms.ModelForm):
    class Meta:
        model = SellerModel
        # fields = "__all__"
        exclude = ('seller',)
