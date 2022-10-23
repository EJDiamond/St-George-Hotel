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
        fields = ('num_adults', 'num_children', 'check_in', 'check_out',)
        labels = {
            "num_adults": "Adults", "num_children": "Children"
        }
        widgets = {
            'num_adults': forms.Select(attrs={'class': 'form-control'}),
            'num_children': forms.Select(attrs={'class': 'form-control'}),
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'phone',)
