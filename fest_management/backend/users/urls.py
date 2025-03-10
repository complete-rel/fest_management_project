from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)  # Creates /api/users/

urlpatterns = [
    path('', include(router.urls)),  # Automatically handles user routes
]
