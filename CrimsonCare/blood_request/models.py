from django.db import models
from django.contrib.auth.models import User
# Create your models here.
GROUP=(('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'),('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'))
BLOOD_GROUP_CHOICES = [
    ('O+', 'O+'), ('O-', 'O-'),
    ('A+', 'A+'), ('A-', 'A-'),
    ('B+', 'B+'), ('B-', 'B-'),
    ('AB+', 'AB+'), ('AB-', 'AB-')
]

class BloodRequest(models.Model):
    STATUS_CHOICES = [('Open', 'Open'), ('Fulfilled', 'Fulfilled')]
    
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES,null=True,blank=True)
    location = models.CharField(max_length=255,null=True,blank=True)
    quantity = models.PositiveIntegerField(null=True,blank=True)
    needed_by = models.DateField(null=True,blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Open',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

class DonationHistory(models.Model):
    STATUS_CHOICES = [('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Canceled', 'Canceled')]
    
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    request = models.ForeignKey(BloodRequest, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
