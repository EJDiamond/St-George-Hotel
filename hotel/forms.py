from django.contrib.auth import models
from django import forms
from .models import Booking
from django.forms import fields, ModelForm
from django.conf import settings
from phonenumber_field.formfields import PhoneNumberField
import datetime
from django.core.exceptions import ValidationError


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    check_in = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}), required=True)
    check_out = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}), required=True)
    phone_number = PhoneNumberField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': ('Please enter in +44 format')}))

    class Meta:
        model = Booking
        fields = ('full_name', 'email', 'phone_number', 'room', 'num_adults', 'num_children', 'check_in', 'check_out',)
        labels = {
            "num_adults": "Adults", "num_children": "Children"
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'num_adults': forms.Select(attrs={'class': 'form-control'}),
            'num_adults': forms.Select(attrs={'class': 'form-control'}),
            'num_children': forms.Select(attrs={'class': 'form-control'}),
            'room': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_check_in(self):
        check_in = self.cleaned_data['check_in']
        if check_in < datetime.date.today():
            raise forms.ValidationError("The date can't be in the past!")
        return check_in

    def clean_check_out(self):
        check_out = self.cleaned_data['check_out']
        if check_out < datetime.date.today():
            raise forms.ValidationError("The date can't be in the past!")
        return check_out


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=50),
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
