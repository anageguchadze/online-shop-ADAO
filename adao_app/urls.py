from django.urls import path
from . import views  

urlpatterns = [
    path('', views.index, name='index'),  
    path('products/', views.product_list, name='product_list'),  
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'), 
    path('login/', views.login_view, name='login'),   
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('orders/', views.orders_view, name='orders'),
    path('add_to_favourites/<int:product_id>/', views.add_to_favourites, name='add_to_favourites'),
    path('favourites/', views.favourites_view, name='favourites'),
    path('favourites/remove/<int:product_id>/', views.remove_from_favourites, name='remove_from_favourites'),
    path('cart/', views.cart_view, name='cart_view'),  # Correct the name of the path
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Path to add to cart
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]
