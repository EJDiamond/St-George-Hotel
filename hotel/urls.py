from hotel import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('rooms', views.rooms, name='rooms'),
    path('spa', views.spa, name='spa'),
    path('booking', views.MakeBooking.as_view(), name='book'),
    path('contactus', views.contactus, name='contactus'),
    path('mybookings', views.my_bookings, name='mybookings'),
    path('edit/<booking_id>', views.edit_booking, name='edit'),
    path('delete/<booking_id>', views.delete_booking, name='delete'),
]
