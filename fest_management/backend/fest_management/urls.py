from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin Panel
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # DRF authentication
    path('api/', include('venues.urls')),  # Venue API
    path('api/', include('events.urls')),  # Event API
    path('api/', include('tickets.urls')),  # Tickets API
    path('api/', include('users.urls')),  # Users API
    path('api/', include('volunteers.urls')),  # Volunteers API
]
