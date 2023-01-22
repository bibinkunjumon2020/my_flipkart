from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from buyer import views as customer_view
from seller import views as company_view
from users import views as users_view
from products import views as products_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register_buyer_wizard/', customer_view.RegisterBuyerWizard.as_view(), name='register_buyer_wizard'),
    path('register_seller_wizard/', company_view.RegisterSellerWizard.as_view(), name='register_seller_wizard'),
    # path('',users_view.HomeView.as_view(),name='home'),
    path('', users_view.ListAllProductsView.as_view(), name='home'),
    path('register', users_view.RegisterView.as_view(), name='register'),
    path('login', users_view.LogInView.as_view(), name='login'),
    path('logout', users_view.LogOutView.as_view(), name='logout'),

    # Buyer
    # path('buyer_register', customer_view.RegistrationView.as_view(), name='buyer_register'),
    path('buyer_login', customer_view.LogInView.as_view(), name='buyer_login'),
    path('buyer_profile', customer_view.BuyerProfile.as_view(), name='buyer_profile'),
    path('buyer_profile_update/<int:pk>',users_view.ProfileUpdateView.as_view(), name='buyer_profile_update'),
    path('buyer_dashboard', customer_view.DashboardBuyer.as_view(), name='buyer_dashboard'),
    # Seller
    # path('seller_register', company_view.RegistrationView.as_view(), name='seller_register'),
    path('seller_login', company_view.LogInView.as_view(), name='seller_login'),
    path('seller_profile', company_view.SellerProfile.as_view(), name='seller_profile'),
    path('product_list/', products_view.ListProductView.as_view(), name='product_list'),  # Seller Dashboard

    # Products
    path('product_add/', products_view.ProductCreateView.as_view(), name='product_add'),
    path('product_update/<int:pk>', products_view.ProductUpdateView.as_view(), name='product_update'),
    path('product_detail/<int:pk>', products_view.ProductDetailView.as_view(), name='product_detail'),
    path('product_delete/<int:pk>', products_view.delete_product, name='product_delete'),

    # Cart
    path('cart/', products_view.CartView.as_view(), name='cart'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
