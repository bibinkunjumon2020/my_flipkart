from django.contrib import admin
from django.urls import path
from customer import views as customer_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',customer_view.RegistrationView.as_view(),name='register'),
    path('register/',customer_view.RegistrationView.as_view(),name='register'),
    path('buyer_login/',customer_view.LogInView.as_view(),name='buyer_login'),
    path('seller_login/',customer_view.LogInView.as_view(),name='seller_login'),
]
