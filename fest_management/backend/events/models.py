from django.db import models
from venues.models import Venue
from django.utils.timezone import now  # Import timezone utility

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateField(default=now)  # Default to today's date
    start_time = models.TimeField(default="12:00:00")  
    end_time = models.TimeField(default="18:00:00")  #
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name="events")
    tickets_available = models.PositiveIntegerField()
    volunteers_needed = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} at {self.venue.name}"

