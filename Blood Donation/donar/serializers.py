from rest_framework import serializers
from . import models
from donation_event.models import DonationHistory
from django.contrib.auth.models import User
from donation_event.serializers import EventSerializer
class DonarSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.DonarProfile
        fields="__all__"


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password=serializers.CharField(required=True)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','confirm_password']

    def save(self):
        username=self.validated_data['username']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        email=self.validated_data['email']
        password=self.validated_data['password']
        confirm_password=self.validated_data['confirm_password']

        if password !=confirm_password:
            raise serializers.ValidationError({'error':"Password dosn't Matched"})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':"Email Already Exists"})
        account=User(username=username,email=email,first_name=first_name,last_name=last_name)
        account.set_password(password)
        account.is_active=False
        account.save()
        return account
    
class LogInSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'blood_group', 'age', 'address', 'last_donation_date', 'is_available')
        read_only_fields = ('email',)


class DonationHistorySerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    
    class Meta:
        model = DonationHistory
        fields = '__all__'
        read_only_fields = ('user', 'date_updated')
