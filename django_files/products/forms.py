from django import forms
from users.models import MyUsers
from .models import Products,Cart

 # buyer Form

class ProductsForm(forms.ModelForm):
    """
    For accessing the inbuilt User model
    """

    title = forms.CharField(required=True, label="Product Title ",
                         widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'title'}))

    description = forms.CharField(required=True, label="Describe the Product",
                                    widget=forms.TextInput(
                                        attrs={"class": "form-control", 'placeholder': 'description'}))
    color = forms.CharField(required=True, label="What's its Color ?",
                                    widget=forms.TextInput(
                                        attrs={"class": "form-control", 'placeholder': 'color'}))
    # category = forms.ChoiceField(required=True, label="Which Category ?",
    #                                 widget=forms.TextInput(
    #                                     attrs={"class": "form-control", 'placeholder': 'category'}))
    price = forms.IntegerField(required=True, label="Market Price ?",
                                    widget=forms.TextInput(
                                        attrs={"class": "form-control", 'placeholder': 'price'}))
    class Meta:
        model = Products
        fields = ['product_pic','title','description','color','price','category','availability']
