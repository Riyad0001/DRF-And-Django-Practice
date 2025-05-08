from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

router=DefaultRouter()

router.register('',views.DonarViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('register/',views.RegistrationView.as_view(),name="register"),
    path('login/',views.LoginApiView.as_view(),name="login"),
    path('logout/',views.LogOutApiView.as_view(),name="logout"),
    path('donar/active/<uid64>/<token>/',views.activation,name="active"),
     path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('events/<int:event_id>/accept/', views.AcceptEventView.as_view(), name='accept-event'),
    
]
urlpatterns += router.urls
