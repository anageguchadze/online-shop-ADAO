from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
import re

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        label="First Name",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'})
    )
    last_name = forms.CharField(
        label="Last Name",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'})
    )
    phone_number = forms.CharField(
        label="Phone Number",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter a 9-digit phone number'})
    )
    street = forms.CharField(
        label="Street",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your street address'})
    )
    house_number = forms.CharField(
        label="House Number",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your house number'})
    )
    apartment_number = forms.CharField(
        label="Apartment Number",
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Optional apartment number'})
    )
    zip_code = forms.CharField(
        label="Zip Code",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your zip code'})
    )
    city = forms.CharField(
        label="City",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your city'})
    )

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phone_number', 'street', 'house_number', 'apartment_number', 'zip_code', 'city']

