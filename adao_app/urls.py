from django.urls import path
from . import views  

urlpatterns = [
    path('', views.index, name='index'),  
    path('products/', views.product_list, name='product_list'),  
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'), 
    path('login/', views.login_view, name='login'),  
    path('cart/', views.cart, name='cart'), 
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    # path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('orders/', views.orders_view, name='orders'),
]
