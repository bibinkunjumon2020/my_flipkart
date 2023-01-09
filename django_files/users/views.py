from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from products.models import Products

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
