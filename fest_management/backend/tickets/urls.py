from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet

router = DefaultRouter()
router.register(r'tickets', TicketViewSet)  # Creates /api/tickets/

urlpatterns = [
    path('', include(router.urls)),  # API endpoints are automatically handled
]
