from hotel import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('booking', views.MakeBooking.as_view(), name='book'),

]
