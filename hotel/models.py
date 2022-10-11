from django.db import models


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
