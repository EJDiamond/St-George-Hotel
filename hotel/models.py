from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


status = (
    ("requested", "Requested"), ("confirmed", "Confirmed"), ("denied", "Denied"))


room_choices = (
    (1, "Poolside View"), (2, "Garden View"), (3, "Ocean View"), (4, "Superior Ocean Suite"))


class Booking(models.Model):
    """ Making a reservation model """
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneNumberField(null=True)
    adult_numbers = ((1, "1 adult"), (2, "2 adults"))
    child_numbers = ((0, "0 children"), (1, "1 child"), (2, "2 children"))
    num_adults = models.IntegerField(choices=adult_numbers, default=1)
    num_children = models.IntegerField(choices=child_numbers, default=0)
    room_type = models.IntegerField(choices=room_choices, default=1)
    check_in = models.DateField()
    check_out = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10, choices=status, default="requested")

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.room_type} booked from {self.check_in} to {self.check_out}"


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return self.name
