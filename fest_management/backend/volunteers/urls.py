from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VolunteerViewSet

router = DefaultRouter()
router.register(r'volunteers', VolunteerViewSet)  # Creates /api/volunteers/

urlpatterns = [
    path('', include(router.urls)),  # Automatically generates API endpoints
]