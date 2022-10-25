from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, View
from django.contrib.auth.models import User
from .models import Booking, Customer, Room, Contact
from .forms import BookingForm, CustomerForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'index.html')


class BookingList(ListView):
    model = Booking


def contactus(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        return HttpResponse("<h1>Thanks for contacting us!</h1>")
    return render(request, 'contact_us.html')


def rooms(request):
    return render(request, 'rooms.html')


def spa(request):
    return render(request, 'spa.html')


class MakeBooking(LoginRequiredMixin, View):
    """ Allows customer to make a booking request if they are logged in"""
    booking_form = BookingForm
    form_class = BookingForm
    template_name = 'bookings.html'
    login_url = 'account_login'
    redirect_field_name = 'index'

    def get(self, request, *args, **kwargs):
        form = self.booking_form()
        rooms = Room.ROOM_CATEGORIES
        return render(request, self.template_name, {'form': form, "rooms": rooms})

    def post(self, request, *args, **kwargs):
        form = self.booking_form(request.POST)

        room_type = request.POST.get("room_type")

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = User.objects.get(username=request.user.username)
            instance.room = Room.objects.filter(category=room_type).first()
            instance.save()

        return render(request, self.template_name, {'form': form})


class CustomerDetails(LoginRequiredMixin, View):
    """ Allows customer to save their personal details """
    customer_form = CustomerForm
    form_class = CustomerForm
    template_name = 'customer_details.html'
    login_url = 'account_login'
    redirect_field_name = 'index'

    def get(self, request, *args, **kwargs):
        form = self.customer_form()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.customer_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        else:
            return render(request, self.template_name, {'form': form})

