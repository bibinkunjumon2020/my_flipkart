from django import forms
from users.models import MyUsers

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

class DateInput(forms.DateInput):
    input_type = 'date'

class RegistrationForm(forms.ModelForm):
    """
    For accessing the inbuilt User model
    """
    seller_name = forms.CharField(required=True, label="Seller Identifying Name ",
                         widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'seller'}))
    seller_reg = forms.CharField(required=True, label="Seller Registration Number/GST",
                         widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'GST/TIN Number'}))

    email = forms.EmailField(required=True, label="Enter Your Email Address",
                             widget=forms.EmailInput(attrs={"class": "form-control",'placeholder': 'Valid Email'}))


# Address Data
    building_name = forms.CharField(required=True, label="House / Office Name & Number ",
                         widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'house/office name'}))

    lane1 = forms.CharField(required=True, label="Address Lane 1 ",
                                    widget=forms.TextInput(
                                        attrs={"class": "form-control", 'placeholder': 'street'}))
    lane2 = forms.CharField(required=True, label="Address Lane 2 ",
                                    widget=forms.TextInput(
                                        attrs={"class": "form-control", 'placeholder': 'street'}))
    state = forms.CharField(required=True, label="State",
                                    widget=forms.TextInput(
                                        attrs={"class": "form-control", 'placeholder': 'state'}))
    district = forms.CharField(required=True, label="District",
                                    widget=forms.TextInput(
                                        attrs={"class": "form-control", 'placeholder': 'district'}))
    place = forms.CharField(required=True, label="Locality",
                                    widget=forms.TextInput(
                                        attrs={"class": "form-control", 'placeholder': 'place/landmark'}))
    pin = forms.CharField(required=True, label="Pincode",
                                    widget=forms.NumberInput(
                                        attrs={"class": "form-control", 'placeholder': '******'}))
    class Meta:
        model = MyUsers
        fields = ['email','seller_name','seller_reg', 'password','founded','phone_number','building_name','lane1','lane2',
                  'state','district','place','country','pin','profile_logo']

        widgets = {
            # "seller_name": forms.TextInput(
            #     attrs={"class": "form-control", 'placeholder': 'seller entity ', 'pattern': '[A-Z a-z]+',
            #            'title': 'Enter Characters Only '}),
            # "seller_reg": forms.TextInput(
            #     attrs={"class": "form-control", 'placeholder': 'seller registration', 'pattern': '[A-Z a-z]+',
            #            'title': 'Enter Characters Only '}),
            "password": forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'create password'}),
            "phone_number":forms.NumberInput(
                attrs={"class": "form-control", 'placeholder': 'Phone number', 'pattern': '[0-9]',
                       'title': 'Enter Numbers Only '}),
            "founded": forms.DateInput(attrs={'type': 'date', }),

        }
