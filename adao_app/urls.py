from django.urls import path
from . import views  

urlpatterns = [
    path('', views.index, name='index'),  
    path('products/', views.product_list, name='product_list'),  
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'), 
    path('login/', views.login_view, name='login'),  
    path('cart/', views.cart, name='cart'), 
]
