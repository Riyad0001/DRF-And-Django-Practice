from . import models
from rest_framework import serializers
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = '__all__'
        read_only_fields = ('creator', 'created_at')

class DonationHistorySerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    
    class Meta:
        model = models.DonationHistory
        fields = '__all__'
        read_only_fields = ('user', 'date_updated')