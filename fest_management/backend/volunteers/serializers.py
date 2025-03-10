from rest_framework import serializers
from .models import Volunteer

class VolunteerSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source="user.username")  # Show username instead of user ID
    event_title = serializers.ReadOnlyField(source="event.title")  # Show event title instead of event ID

    class Meta:
        model = Volunteer
        fields = ['id', 'user', 'user_username', 'event', 'event_title', 'role', 'status', 'signup_date']
