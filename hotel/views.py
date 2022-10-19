from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .models import Booking, Customer
from .forms import BookingForm
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'index.html')


class MakeBooking(View):
    booking_form = BookingForm
    template_name = 'bookings.html'

    def get(self, request, *args, **kwargs):
        form = self.booking_form()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.booking_form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
