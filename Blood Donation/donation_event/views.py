from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from . import models
# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.Event.objects.exclude(creator=self.request.user)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class MyEventsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.Event.objects.filter(creator=self.request.user)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class AcceptEventView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, event_id):
        try:
            event = models.Event.objects.get(id=event_id)
        except models.Event.DoesNotExist:
            return Response({'detail': 'Event not found.'}, status=status.HTTP_404_NOT_FOUND)

        if event.creator == request.user:
            return Response({'detail': 'Cannot accept your own event.'}, status=status.HTTP_400_BAD_REQUEST)

        donation, created = models.DonationHistory.objects.get_or_create(
            user=request.user,
            event=event,
            defaults={'status': 'accepted'}
        )
        if not created:
            return Response({'detail': 'Event already accepted.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 'Event accepted.'}, status=status.HTTP_201_CREATED)