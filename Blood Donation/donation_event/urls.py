from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'events', views.EventViewSet, basename='event')
router.register(r'my-events', views.MyEventsViewSet, basename='my-event')
router.register(r'donation-history', views.DonationHistoryViewSet, basename='donation-history')

urlpatterns = [
    
    path('events/<int:event_id>/accept/', views.AcceptEventView.as_view(), name='accept-event'),
    path('donors/', views.DonorListView.as_view(), name='donor-list'),
    path('', include(router.urls)),
]