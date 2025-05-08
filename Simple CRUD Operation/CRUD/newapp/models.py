from django.db import models

# Create your models here.

class Member((models.Model)):
    first_name=models.CharField(max_length=60)
    last_name=models.CharField(max_length=60)
    address=models.TextField()

    def __str__(self):
        return self.first_name