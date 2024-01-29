from django.contrib import admin
from django.urls import path, include
from .api import api
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from authentication.views import CustomTokenObtainPairView, CustomTokenRefreshView



urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/authentication/', include('authentication.urls')),
    path('api/', api.urls),

]

