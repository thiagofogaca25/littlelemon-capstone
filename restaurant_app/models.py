from django.db import models
from django.contrib.auth.models import User


class MenuItem(models.Model):
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.PositiveIntegerField(default=0)


class Meta:
    ordering = ["title"]


def __str__(self):
    return f"{self.title}"


class Booking(models.Model):
    name = models.CharField(max_length=120)
    no_of_guests = models.PositiveIntegerField()
    booking_date = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


class Meta:
    ordering = ["-booking_date"]


def __str__(self):
    return f"{self.name} @ {self.booking_date}"