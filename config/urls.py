from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
TokenObtainPairView,
TokenRefreshView,
)


urlpatterns = [
path("admin/", admin.site.urls),
# HTML estático mínimo
path("", TemplateView.as_view(template_name="index.html"), name="home"),
# API
path("api/", include("restaurant.urls")),
# Auth JWT
path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]