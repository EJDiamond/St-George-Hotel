from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from .models import Booking, Customer
from .forms import BookingForm, CustomerForm


def index(request):
    return render(request, 'index.html')


class MakeBooking(View):

    def post(self, request, User=User, *args, **kwargs):
        booking_form = BookingForm(data=request.POST)
        customer_form = CustomerForm(data=request.POST)

        return render(
            request, 'bookings.html')