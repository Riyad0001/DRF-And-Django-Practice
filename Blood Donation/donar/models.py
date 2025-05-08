from django.db import models
from django.contrib.auth.models import User
BLOOD_GROUP_CHOICES = [
    ('O+', 'O+'), ('O-', 'O-'),
    ('A+', 'A+'), ('A-', 'A-'),
    ('B+', 'B+'), ('B-', 'B-'),
    ('AB+', 'AB+'), ('AB-', 'AB-')
]
STATUS=(
    ('Received', 'Received'), ('Donated', 'Donated'), ('Canceled', 'Canceled')
)
class BloodGroup(models.Model):
    blood_group=models.CharField(max_length=10)
class City(models.Model):
    city=models.CharField(max_length=100)
class DonarProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.IntegerField()
    full_address=models.CharField(max_length=150)
    blood_group = models.OneToOneField(BloodGroup,on_delete=models.CASCADE)
    city=models.OneToOneField(City,on_delete=models.CASCADE)
    last_donation_date=models.DateField(null=True,blank=True)
    is_available=models.BooleanField(default=True)
