from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from customer import views as customer_view
from company import views as company_view
from users import views as users_view
from products import views as products_view
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',users_view.HomeView.as_view(),name='home'),
    path('',users_view.ListAllProductsView.as_view(),name='home'),
    path('buyer_register',customer_view.RegistrationView.as_view(),name='buyer_register'),
    path('seller_register',company_view.RegistrationView.as_view(),name='seller_register'),
    path('register',users_view.RegisterView.as_view(),name='register'),
    path('buyer_login',customer_view.LogInView.as_view(),name='buyer_login'),
    path('seller_login',company_view.LogInView.as_view(),name='seller_login'),
    path('login',users_view.LogInView.as_view(),name='login'),
    path('buyer_profile',customer_view.BuyerProfile.as_view(),name='buyer_profile'),
    path('seller_profile',company_view.SellerProfile.as_view(),name='seller_profile'),
    # Products
    path('product_add/',products_view.ProductCreateView.as_view(),name='product_add'),
    path('product_update/<int:pk>',products_view.ProductUpdateView.as_view(),name='product_update'),
    path('product_list/',products_view.ListProductView.as_view(),name='product_list'),
    path('product_detail/<int:pk>',products_view.ProductDetailView.as_view(),name='product_detail'),
    path('product_delete/<int:pk>',products_view.delete_product,name='product_delete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
