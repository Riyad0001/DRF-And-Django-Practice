from django.contrib import admin
from .models import Intersection, TrafficLight, TrafficEvent, UserFeedback,TrafficViolation

admin.site.register(Intersection)
admin.site.register(TrafficLight)
admin.site.register(TrafficEvent)
admin.site.register(UserFeedback)
admin.site.register(TrafficViolation)