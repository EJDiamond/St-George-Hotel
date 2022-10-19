from django.contrib.auth import models
from django import forms
from .models import Customer, Booking
from django.forms import fields, ModelForm
from django.conf import settings
from phonenumber_field.formfields import PhoneNumberField


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('customer', 'num_adults', 'num_children', 'room', 'check_in', 'check_out',)


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'phone',)
