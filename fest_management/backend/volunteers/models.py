from django.db import models
from django.contrib.auth import get_user_model
from events.models import Event  
from django.utils.timezone import now

User = get_user_model()

class Volunteer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="volunteer_roles")  # The user who is volunteering
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="volunteers")  # The event they are volunteering for
    role = models.CharField(max_length=100)  # Volunteer role (e.g., security, ticketing, setup)
    status = models.CharField(
        max_length=10, 
        choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')],
        default='pending'
    )
    signup_date = models.DateTimeField(default=now)  # When the user signed up

    def __str__(self):
        return f"{self.user.username} volunteering for {self.event.title} as {self.role}"
