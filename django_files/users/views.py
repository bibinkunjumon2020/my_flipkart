from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView,View
from products.models import Products
from django.contrib.auth import login, logout, authenticate

class HomeView(TemplateView):
    template_name = "eventWebsite/home.html"


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

