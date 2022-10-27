from django.contrib import admin
from .models import Booking, Contact

# Register your models here.


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'room_type', 'num_adults', 'num_children', 'check_in', 'check_out', 'status')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'subject')

