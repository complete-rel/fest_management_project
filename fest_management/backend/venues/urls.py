from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VenueViewSet

# Use a DRF router to automatically handle routes
router = DefaultRouter()
router.register(r'venues', VenueViewSet)  # Creates /api/venues/

urlpatterns = [
    path('api/', include(router.urls)),  # Automatically handles all venue endpoints
]
