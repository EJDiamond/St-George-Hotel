from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    ROOM_CATEGORIES = (
        ('PSR', 'Poolside'),
        ('GVR', 'Garden View'),
        ('OVR', 'Ocean View'),
        ('SOS', 'Superior Ocean Suite')
    )

    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    adults = models.IntegerField()
    children = models.IntegerField()

    def __str__(self):
        return f'{self.number}. {self.category} for {self.adults} adults and {self.children} children'


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f'{self.user} has requested to book {self.room} from {self.check_in} to {self.check_out}'
