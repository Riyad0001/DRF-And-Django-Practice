from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BloodRequest, DonationHistory
from .serializers import *
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator

class BloodRequestListCreateView(generics.ListCreateAPIView):
    serializer_class = BloodRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = BloodRequest.objects.filter(status='Open')
        
        # Get filter parameters from request
        blood_group = self.request.query_params.get('blood_group')
        location = self.request.query_params.get('location')
        min_quantity = self.request.query_params.get('min_quantity')
        max_quantity = self.request.query_params.get('max_quantity')
        needed_by = self.request.query_params.get('needed_by')

        # Apply filters
        if blood_group:
            queryset = queryset.filter(blood_group__iexact=blood_group)
        if location:
            queryset = queryset.filter(location__icontains=location)
        if min_quantity:
            queryset = queryset.filter(quantity__gte=min_quantity)
        if max_quantity:
            queryset = queryset.filter(quantity__lte=max_quantity)
        if needed_by:
            queryset = queryset.filter(needed_by__lte=needed_by)
            
        return queryset

    def perform_create(self, serializer):
        serializer.save(requester=self.request.user)

class AcceptRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            blood_request = BloodRequest.objects.get(pk=pk)
            if blood_request.requester == request.user:
                return Response({'detail': 'Cannot accept your own request'}, status=400)
            
            DonationHistory.objects.create(
                donor=request.user,
                request=blood_request,
                status='Accepted'
            )
            return Response({'detail': 'Request accepted'})
        except BloodRequest.DoesNotExist:
            return Response({'detail': 'Request not found'}, status=404)
