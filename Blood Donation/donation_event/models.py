from django.db import models
from django.contrib.auth.models import User
from donar.models import BloodGroup
# Create your models here.
class Event(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    blood_group_needed = models.OneToOneField(BloodGroup,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class DonationHistory(models.Model):
    STATUS_CHOICES = [
        ('accepted', 'Accepted'),
        ('canceled', 'Canceled'),
        ('donated', 'Donated'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    date_updated = models.DateTimeField(auto_now=True)