from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, BookingViewSet, RegisterView


router = DefaultRouter()
router.register(r"menu", MenuItemViewSet, basename="menu")
router.register(r"bookings", BookingViewSet, basename="booking")


urlpatterns = [
path("", include(router.urls)),
path("auth/register/", RegisterView.as_view(), name="register"),
]