from rest_framework import serializers
from . import models

class BloodRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BloodRequest
        fields = '__all__'
        read_only_fields = ('requester', 'status')

class DonationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DonationHistory
        fields = '__all__'
        read_only_fields = ('donor', 'created_at')