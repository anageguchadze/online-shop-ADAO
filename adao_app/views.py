from .models import Product, UserProfile
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
            messages.success(request, "Successfully logged in!")
            return redirect('dashboard')  # გადამისამართება დეშბორდზე
        else:
            messages.error(request, "Invalid email or password.")
    return render(request, 'adao_app/login.html')


@login_required
def profile_view(request):
    # Ensure the profile exists
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if created:
        # If a new profile was created, ensure all fields are empty
        user_profile.first_name = ''
        user_profile.last_name = ''
        user_profile.phone_number = ''
        user_profile.street = ''
        user_profile.house_number = ''
        user_profile.apartment_number = ''
        user_profile.zip_code = ''
        user_profile.city = ''
        user_profile.save()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors below.")
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
    return redirect('index')  # გადამისამართება მთავარ გვერდზე


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