from django.contrib.auth import models
from django import forms
from .models import Customer, Booking
from django.forms import fields, ModelForm
from django.conf import settings
from phonenumber_field.formfields import PhoneNumberField


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    check_in = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}))
    check_out = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Booking
        fields = ('customer', 'num_adults', 'num_children', 'check_in', 'check_out',)
        labels = {
            "num_adults": "Adults", "num_children": "Children"
        }
        widgets = {
            'num_adults': forms.Select(attrs={'class': 'form-control'}),
            'num_children': forms.Select(attrs={'class': 'form-control'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
        }


class CustomerForm(forms.ModelForm):
    phone = PhoneNumberField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'phone',)

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=50),
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
