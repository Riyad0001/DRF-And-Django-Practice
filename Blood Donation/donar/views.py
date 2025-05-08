from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives,EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.shortcuts import redirect
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status, viewsets

from . import serializers
from . import models
# Create your views here.

class DonarViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DonarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    # Add explicit queryset attribute
    queryset = models.DonarProfile.objects.all()
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Get filter parameters
        blood_group = self.request.query_params.get('blood_group')
        address = self.request.query_params.get('address')
        min_age = self.request.query_params.get('min_age')
        max_age = self.request.query_params.get('max_age')
        is_available = self.request.query_params.get('is_available')

        # Apply filters
        if blood_group:
            queryset = queryset.filter(blood_group__iexact=blood_group)
        if address:
            queryset = queryset.filter(address__icontains=address)
        if min_age:
            queryset = queryset.filter(age__gte=min_age)
        if max_age:
            queryset = queryset.filter(age__lte=max_age)
        if is_available:
            queryset = queryset.filter(is_available=is_available.lower() == 'true')
            
        return queryset


class RegistrationView(APIView):
    serializer_class=serializers.RegistrationSerializer

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            token=default_token_generator.make_token(user)
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link=f"http://127.0.0.1:8000/donar/active/{uid}/{token}"
            email_subject="Active your account"
            email_body=render_to_string('active_mail.html',{'confirm_link':confirm_link})
            email=EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body,"text/html")
            email.send()
            return Response("Check your Email To confirmation link for active")
        return Response(serializer.errors)
          
def activation(request,uid64,token):
    try:
        uid=urlsafe_base64_decode(uid64).decode()
        user=User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        return redirect("login")
    else:
        return redirect("register")
    
class LoginApiView(APIView):
    def post(self,request):
        serializer=serializers.LogInSerializer(data=self.request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']

            user=authenticate(username=username,password=password)

            if user:
                token,_=Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request,user)
                return Response({'token':token.key,'user_id':user.id})
            return Response('error',"Invalid Credential")
        return Response(serializer.errors)

class LogOutApiView(APIView):
    def get(self,request):
        request.user.auth_token.delete()
        logout(request)
        return redirect("login")
    
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = serializers.UserProfileSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = serializers.UserProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DonationHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.DonationHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.DonationHistory.objects.filter(user=self.request.user)

class DonorListView(generics.ListAPIView):
    serializer_class = serializers.UserProfileSerializer
    queryset = User.objects.filter(is_available=True)
    filter_fields = ['blood_group']
    search_fields = ['address']
    
