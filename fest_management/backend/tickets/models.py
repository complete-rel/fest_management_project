from django.db import models
from django.contrib.auth import get_user_model
from events.models import Event  # Import Event model

User = get_user_model()

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('canceled', 'Canceled'),
    ]

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="tickets")  # Links ticket to event
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tickets")  # Links ticket to user
    purchase_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Ticket for {self.event.title} - {self.user.username}"


