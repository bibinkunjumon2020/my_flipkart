from django.shortcuts import render, redirect

from products.models import Products,Cart
from products.forms import ProductsForm
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView, CreateView, TemplateView, UpdateView


# Products - Add,Edit,Delete,Detail

class ProductCreateView(CreateView):
    """
    CreateView used to new post creation with form given data,depends on model
    """

    template_name = "eventWebsite/product_add.html"
    model = Products
    form_class = ProductsForm
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        """
        Used to add instance value 'user' to the creation form
        """
        form.instance.seller = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    """
    UpdateView used to update the detail of a specific post
    """

    model = Products
    template_name = "eventWebsite/product_add.html"
    form_class = ProductsForm
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        return super().form_valid(form)  # It helps to load existing value to the form


class ListProductView(ListView):  # list products by that seller # Seller Dashboard
    """
    ListView used to list of posts with form given data,depends on model
    """
    template_name = "eventWebsite/product_list.html"
    model = Products
    context_object_name = 'products'  # with this data can be accessed in front end html

    def get_queryset(self):
        """
        this specific query is used to run this View
        """
        return Products.objects.filter(seller=self.request.user)


class ProductDetailView(DetailView):
    """
    DetailView used to show the detail of a specific post
    """
    template_name = "eventWebsite/product_detail.html"
    model = Products
    context_object_name = "product"  # with this data can be accessed in front end html


def delete_product(request, *args, **kwargs):  # path : /delete/<int:id>
    """
    It's a function for deleting list entries
    """
    Products.objects.get(id=kwargs.get('pk')).delete()
    return redirect("product_list")

class CartView(ListView):
    template_name = "eventWebsite/cart.html"
    model = Cart
    context_object_name = "products"
    def get_queryset(self):
        """
        this specific query is used to run this View
        """
        return Cart.objects.filter( buyer=self.request.user)


