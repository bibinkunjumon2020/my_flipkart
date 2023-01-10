from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View,ListView
from .forms import RegistrationForm, LoginForm
from users.models import MyUsers
from products.models import Products
class RegistrationView(View): # Customer SignUp
    """ Method for accepting user credentials and creating a User
        Django inbuilt User Model is used.
    """
    def get(self, request, *args, **kwargs):
        """
        Rendering form fields
        """
        form = RegistrationForm()
        return render(request, "eventWebsite/registration.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        """
        Saving the form data in Database.
        """
        print("######### Form Enter")

        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("######### Form Valid")
            password = form.cleaned_data.get('password')
            user = form.save(commit=False)
            user.set_password(password)
            user.role = MyUsers.seller
            user.save()
            print("Registration Success",user)
            return redirect('seller_login')  # Success redirected to Log-in View
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
                return redirect('product_list')
            else:
                print("Failed ..No such User")
                return redirect("register")

        else:
            return render(request, "eventWebsite/login.html", context={"form": form})

        return render(request, "eventWebsite/login.html", {"form": form})

class LogOutView(View):
    """User logout class """
    def get(self, request, *args, **kwargs):
        logout(request)  # inbuilt func
        return redirect("home")

class SellerProfile(View):  # View the profile of seller from registration
    def get(self,request):
        # print("@@@@@@@@@@",request.user,request.user.email,request.user.phone_number)
        seller = MyUsers.objects.filter(email=self.request.user.email)
        return render(request, "eventWebsite/seller-profile.html", context={"seller": seller})

