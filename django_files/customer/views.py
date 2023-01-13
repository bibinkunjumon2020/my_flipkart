from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View, TemplateView, ListView
from .forms import RegistrationForm, LoginForm
from users.models import MyUsers
from products.models import Products, Cart
from django.http import HttpResponse


class RegistrationView(View):  # Customer SignUp
    """ Method for accepting user credentials and creating a User
        Django inbuilt User Model is used.
    """

    def get(self, request, *args, **kwargs):
        """
        Rendering form fields
        """
        form = RegistrationForm()
        # return render(request, "eventWebsite/home.html", context={"form": form})
        return render(request, "eventWebsite/registration.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        """
        Saving the form data in Database.
        """
        print("######### Form Enter")

        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            print("######### Form Valid")
            password = form.cleaned_data.get('password')
            user = form.save(commit=False)
            user.set_password(password)
            user.role = MyUsers.buyer
            user.save()
            print("Registration Success", user)
            return redirect('buyer_login')  # Success redirected to Log-in View
        else:
            print("#######Form Error")
            return render(request, "eventWebsite/registration.html", context={"form": form})


class LogInView(View):
    """ User can log in with username and password.It uses built authenticate function """

    def get(self, request, *args, **kwargs):
        """
                Rendering form fields
                """
        form = LoginForm()
        return render(request, "eventWebsite/login.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        """
            Use input credentials for authenticating
                """
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            print(email, password)
            print(user)
            if user is not None:
                print("Authenticated Successfully")
                login(request, user)
                print("Login Success")
                return redirect('buyer_dashboard')
                # return redirect('buyer_profile')
            else:
                print("Failed ..No such User")
                return redirect("register")

        else:
            return render(request, "eventWebsite/login.html", context={"form": form})

        return render(request, "eventWebsite/login.html", {"form": form})


class BuyerProfile(View):
    def get(self, request):
        print("@@@@@@@@@@", request.user, request.user.email, request.user.phone_number)
        buyer = MyUsers.objects.filter(email=self.request.user.email)
        # for buy in buyer:
        #    print("///////",buy.first_name)
        return render(request, "eventWebsite/buyer-profile.html", context={"buyer": buyer})


class DashboardBuyer(ListView):
    """
       ListView used to list of posts with form given data,depends on model
       """
    template_name = "eventWebsite/dashboard.html"
    model = Products
    context_object_name = 'products'  # with this data can be accessed in front end html

    def get_queryset(self):
        """
        this specific query is used to run this View
        """
        return Products.objects.all()

    def post(self, *args, **kwargs):
        btn_add_cart = self.request.POST.get('btn_add_cart')
        if btn_add_cart == "add_cart":
            print("&&&& How to add cart")
            Cart.objects.create()
        return redirect("cart")
    # return HttpResponse(status=200)
