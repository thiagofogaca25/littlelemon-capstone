from django.contrib import admin
from .models import MenuItem, Booking


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "inventory")
    search_fields = ("title",)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "no_of_guests", "booking_date", "created_by")
    search_fields = ("name",)
    list_filter = ("booking_date",)