from rest_framework import viewsets
from .models import Venue
from .serializers import VenueSerializer

class VenueViewSet(viewsets.ModelViewSet):  # Handles all CRUD operations
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    lookup_field = "slug"  # Uses slug instead of ID
