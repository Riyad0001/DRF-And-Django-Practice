# traffic/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('intersections/', views.intersection_view, name='intersections'),
    path('traffic_lights/<int:intersection_id>/', views.traffic_light_view, name='traffic_lights'),
    path('traffic_events/', views.traffic_event_view, name='traffic_events'),
    path('user_feedback/', views.user_feedback_view, name='user_feedback'),
    path('user_profile/', views.user_profile_view, name='user_profile'),
    path('traffic_violation/', views.traffic_violation_view, name='traffic_violation'),
    path('route_optimization/', views.route_optimization_view, name='route_optimization'),
    path('user_dashboard/', views.user_dashboard_view, name='user_dashboard'),
    path('admin_dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('analytics/', views.analytics_view, name='analytics'),
    path('notification_settings/', views.notification_settings_view, name='notification_settings'),
    path('feedback_summary/', views.feedback_summary_view, name='feedback_summary'),
    path('real_time_map/', views.real_time_map_view, name='real_time_map'),
    path('help_support/', views.help_support_view, name='help_support'),
]


