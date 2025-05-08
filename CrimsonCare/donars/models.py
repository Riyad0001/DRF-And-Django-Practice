from django.db import models
from django.contrib.auth.models import User
from blood_request.models import BloodRequest
# Create your models here.
BLOOD_GROUP_CHOICES = [
    ('O+', 'O+'), ('O-', 'O-'),
    ('A+', 'A+'), ('A-', 'A-'),
    ('B+', 'B+'), ('B-', 'B-'),
    ('AB+', 'AB+'), ('AB-', 'AB-')
]
STATUS=(
    ('Received', 'Received'), ('Donated', 'Donated'), ('Canceled', 'Canceled')
)
class DonarProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.IntegerField()
    address=models.CharField(max_length=150)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES,null=True,blank=True)
    last_donation_date=models.DateField(null=True,blank=True)
    is_available=models.BooleanField(default=True)
              
            
            
class Event(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    blood_group_needed = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    is_active = models.BooleanField(default=True,null=True,blank=True)

class DonationHistory(models.Model):
    STATUS_CHOICES = [
        ('accepted', 'Accepted'),
        ('canceled', 'Canceled'),
        ('donated', 'Donated'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,null=True,blank=True)
    date_updated = models.DateTimeField(auto_now=True,null=True,blank=True)

