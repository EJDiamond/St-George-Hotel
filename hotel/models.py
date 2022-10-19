from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


status = (
    ("requested", "requested"), ("confirmed", "confirmed"), ("denied", "denied"))


class Room(models.Model):
    """ Hotel rooms model """
    ROOM_CATEGORIES = (
        ('PSR', 'Poolside'),
        ('GVR', 'Garden View'),
        ('OVR', 'Ocean View'),
        ('SOS', 'Superior Ocean Suite')
    )

    number = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    adults = models.IntegerField()
    children = models.IntegerField()

    def __str__(self):
        return str(self.category)


class Customer(models.Model):
    """ Customer personal info model """
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, null=True, blank=False)
    phone = PhoneNumberField(null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Booking(models.Model):
    """ Making a reservation model """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    adult_numbers = ((1, "1 adult"), (2, "2 adults"))
    child_numbers = ((0, "0 children"), (1, "1 child"), (2, "2 children"))
    num_adults = models.IntegerField(choices=adult_numbers, default=1)
    num_children = models.IntegerField(choices=child_numbers, default=0)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    check_in = models.DateField()
    check_out = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10, choices=status, default="requested")

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'{self.room} booked by {self.customer}'
