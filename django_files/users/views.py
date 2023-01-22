from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView,View,UpdateView
from products.models import Products
from django.contrib.auth import login, logout, authenticate
from users.forms import RegistrationFormOne,RegistrationFormAddress
from buyer.forms import RegistrationBuyerForm
from seller.forms import RegistrationSellerForm
from .models import MyUsers
# Wizard form
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import default_storage
class RegisterWizard(SessionWizardView):
    form_list = [RegistrationFormOne,RegistrationBuyerForm,RegistrationFormAddress]
    file_storage = default_storage

# class HomeView(TemplateView):
#     template_name = "eventWebsite/home.html"


class LogInView(TemplateView):
    template_name = "eventWebsite/home_login.html"


class RegisterView(TemplateView):
    template_name = "eventWebsite/home_register.html"


class ListAllProductsView(ListView):
    """
    ListView used to list of posts with form given data,depends on model
    """
    template_name = "eventWebsite/home.html"
    model = Products
    context_object_name = 'products'  # with this data can be accessed in front end html

    def get_queryset(self):
        """
        this specific query is used to run this View
        """
        return Products.objects.all()

class LogOutView(View):
    """User logout class """

    def get(self, request, *args, **kwargs):
        logout(request)  # inbuilt func
        return redirect("home")

class ProfileUpdateView(UpdateView):
    """
    UpdateView used to update the detail of a specific post
    """

    model = MyUsers
    template_name = "eventWebsite/buyer-profile.html"
    form_class = RegistrationFormAddress
    success_url = reverse_lazy('buyer_dashboard')

    def form_valid(self, form):
        return super().form_valid(form)  # It helps to load existing value to the form

