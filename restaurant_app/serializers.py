from rest_framework import serializers
from .models import MenuItem, Booking
from django.contrib.auth.models import User


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["id", "title", "price", "inventory"]


class BookingSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")


class Meta:
    model = Booking
    fields = ["id", "name", "no_of_guests", "booking_date", "created_by"]


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


class Meta:
    model = User
    fields = ["id", "username", "email", "password"]


def create(self, validated_data):
    user = User.objects.create_user(
    username=validated_data["username"],
    email=validated_data.get("email", ""),
    password=validated_data["password"],
    )
    
    return user