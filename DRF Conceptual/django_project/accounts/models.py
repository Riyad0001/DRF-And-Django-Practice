from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    user_type_choice={
        {'admin','Admin'},
        {'viewer','Viewer'},
        {'editor','Editor'}
    }
    user_type=models.CharField(max_length=20,choices=user_type_choice,default="viewer")
