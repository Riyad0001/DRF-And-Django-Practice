from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

urlpatterns = [
    path('blood-requests/', views.BloodRequestListCreateView.as_view(), name='blood-requests'),
    path('accept-request/<int:pk>/', views.AcceptRequestView.as_view(), name='accept-request'),
]
