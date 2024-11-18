from .models import Product, UserProfile, Cart, Favourite
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.models import User 
from .forms import CustomUserCreationForm, UserProfileForm
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None and user.check_password(password):
            login(request, user)
            # Do not show success message here
            return redirect('dashboard')  # Redirect to dashboard
        else:
            # Only show an error message for invalid login
            messages.error(request, "Invalid email or password.")
    return render(request, 'adao_app/login.html')


@login_required
def profile_view(request):
    # Try to get or create the user's profile
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')  # Redirect back to profile after save
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'adao_app/profile.html', {'form': form})



@login_required
def profile(request):
    try:
        profile = request.user.profile  # თუ პროფილი არსებობს
    except UserProfile.DoesNotExist:
        profile = None  # თუ არ არსებობს, ახალ პროფილზე გადაგვიყვანს

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()  # შენახვა
            return redirect('profile')  # წარმატებული შენახვის შემდეგ გვერდზე დაბრუნება
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'adao_app/profile.html', {'form': form})


@login_required
def dashboard_view(request):
    return render(request, 'adao_app/dashboard.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # მომხმარებლის რეგისტრაცია
            user = form.save()
            email = form.cleaned_data.get('email')
            user.email = email  # ელ. ფოსტა
            user.save()

            messages.success(request, "Account created successfully!")
            login(request, user)  # ავტორიზაცია
            return redirect('index')
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'adao_app/register.html', {'form': form})


@login_required
def orders_view(request):
    return render(request, 'adao_app/orders.html')


def logout_view(request):
    logout(request)  # მომხმარებელი გავიდა სისტემიდან
    return redirect('login')  

def index(request):
    return render(request, 'adao_app/index.html')


def product_list(request):
    products = Product.objects.all()  
    return render(request, 'adao_app/product_list.html', {'products': products})


def about(request):
    return render(request, 'adao_app/about.html')


def contact(request):
    return render(request, 'adao_app/contact.html')


def cart(request):
    return render(request, 'adao_app/cart.html')

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    # Check if the product is already in the cart
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if created:
        messages.success(request, f'{product.name} added to your cart.')
    else:
        # If the item is already in the cart, update the quantity
        cart_item.quantity += 1
        cart_item.save()
        messages.info(request, f'{product.name} quantity updated in your cart.')

    # Redirect to the cart view (not product list)
    return redirect('product_list')  # Redirect to the cart page to view updated items




# View for displaying the Cart
@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)  # Get all cart items for the logged-in user

    if not cart_items:
        messages.info(request, "Your cart is empty.")  # Show a message if the cart is empty

    return render(request, 'adao_app/cart.html', {'cart_items': cart_items})



@login_required
def remove_from_cart(request, product_id):
    try:
        # Get the cart item associated with the user and product
        cart_item = Cart.objects.get(user=request.user, product_id=product_id)
        cart_item.delete()  # Delete the item
        messages.success(request, "Item removed from your cart.")
    except Cart.DoesNotExist:
        messages.error(request, "Item not found in your cart.")

    return redirect('cart_view')  # Redirect back to the cart page



# Add product to Favourites
@login_required
def add_to_favourites(request, product_id):
    product = Product.objects.get(id=product_id)

    # Check if the product is already in the favourites
    favourite_item, created = Favourite.objects.get_or_create(user=request.user, product=product)

    if created:
        messages.success(request, f'{product.name} added to your favourites!')
    else:
        messages.info(request, f'{product.name} is already in your favourites!')

    return redirect('product_list')  # Redirect back to product list or favourites page


@login_required
def favourites_view(request):
    favourite_items = Favourite.objects.filter(user=request.user)

    return render(request, 'adao_app/favourites.html', {'favourite_items': favourite_items})


@login_required
def remove_from_favourites(request, product_id):
    try:
        # Get the favorite item associated with the user and product
        favourite_item = Favourite.objects.get(user=request.user, product_id=product_id)
        favourite_item.delete()  # Delete the item
        messages.success(request, "Item removed from your favourites.")
    except Favourite.DoesNotExist:
        messages.error(request, "Item not found in your favourites.")

    return redirect('favourites')  # Redirect back to the favourites page
