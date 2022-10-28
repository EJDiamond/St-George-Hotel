from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from django.contrib.auth.models import User
from .models import Booking, Contact
from .forms import BookingForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


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
        messages.success(request, 'Thanks for contacting us, we will respond shortly.')
        return render(request, 'index.html')

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
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.booking_form(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = User.objects.get(username=request.user.username)
            instance.save()
            messages.success(request, 'Booking request submitted successfully, check back in "My Bookings" for approved status')
            return render(request, "index.html", {'form': form})
        else:
            messages.error(request, 'You need to pick a date in the future.')

        return render(request, "bookings.html", {'form': form})


def my_bookings(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'my_bookings.html', context)


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Booking has been modified, check back for booking status.')
            return redirect('mybookings')
    form = BookingForm(instance=booking)
    context = {
        'form': form
        }
    return render(request, 'edit_booking.html', context)


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    messages.success(
        request, 'You have successfully cancelled your booking')
    return redirect('mybookings')
