# traffic/models.py
from django.db import models
from django.contrib.auth.models import User

class Intersection(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

class TrafficLight(models.Model):
    intersection = models.ForeignKey('Intersection', on_delete=models.CASCADE)
    status = models.CharField(max_length=10)  # e.g., 'Red', 'Green', 'Yellow'
    last_updated = models.DateTimeField(auto_now=True)

class TrafficEvent(models.Model):
    intersection = models.ForeignKey('Intersection', on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50)  # e.g., 'Accident', 'Heavy Traffic'
    timestamp = models.DateTimeField(auto_now_add=True)

class UserFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    intersection = models.ForeignKey('Intersection', on_delete=models.CASCADE)
    feedback = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class TrafficViolation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    intersection = models.ForeignKey('Intersection', on_delete=models.CASCADE)
    violation_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
