from django import forms
from users.models import MyUsers


class RegistrationFormOne(forms.ModelForm):
    email = forms.EmailField(required=True, label="Enter Your Email Address",
                             widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'Valid Email'}))

    class Meta:
        model = MyUsers
        fields = ['email', 'password', ]

        widgets = {
            "password": forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'create password'}),
        }


class RegistrationFormAddress(forms.ModelForm):
    building_name = forms.CharField(required=True, label="House / Office Name & Number ",
                                    widget=forms.TextInput(
                                        attrs={"class": "form-control", 'placeholder': 'house/office name'}))

    lane1 = forms.CharField(required=True, label="Address Lane 1 ",
                            widget=forms.TextInput(
                                attrs={"class": "form-control", 'placeholder': 'street'}))
    lane2 = forms.CharField(required=True, label="Address Lane 2 ",
                            widget=forms.TextInput(
                                attrs={"class": "form-control", 'placeholder': 'street'}))
    place = forms.CharField(required=True, label="place",
                            widget=forms.TextInput(
                                attrs={"class": "form-control", 'placeholder': 'place/landmark'}))
    state = forms.CharField(required=True, label="State",
                            widget=forms.TextInput(
                                attrs={"class": "form-control", 'placeholder': 'state'}))
    district = forms.CharField(required=True, label="District",
                               widget=forms.TextInput(
                                   attrs={"class": "form-control", 'placeholder': 'district'}))
    pin = forms.CharField(required=True, label="Pincode",
                          widget=forms.NumberInput(
                              attrs={"class": "form-control", 'placeholder': '******'}))

    class Meta:
        model = MyUsers
        fields = ['profile_logo', 'building_name', 'lane1', 'lane2', 'place',
                  'state', 'district', 'country', 'pin', 'phone_number', ]

        widgets = {
            "phone_number": forms.NumberInput(
                attrs={"class": "form-control", 'placeholder': 'Phone number', 'pattern': '[0-9]',
                       'title': 'Enter Numbers Only '}),
        }
