from django.shortcuts import render
from .models import Product
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.models import User 
from .forms import CustomUserCreationForm


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']  # ელ. ფოსტის მიღება
        password = request.POST['password']  # პაროლი

        # ელ. ფოსტის მიხედვით მოძებნე მომხმარებელი
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        # თუ მომხმარებელი მოიძებნა, დაამოწმე პაროლი
        if user is not None and user.check_password(password):
            login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect('index')  # გადამისამართება მთავარ გვერდზე
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, 'adao_app/login.html')  # ლოგინის გვერდის გაშვება


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