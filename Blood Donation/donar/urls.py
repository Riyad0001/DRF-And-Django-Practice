from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
router=DefaultRouter()
router.register("",views.PatientViewSet)

urlpatterns = [
    path('list/',include(router.urls)),
    path('donors/', views.DonorListView.as_view(), name='donor-list'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('register/',views.RegistrationApiView.as_view()),
    path('login/',views.LoginApiView.as_view(),name="login"),
    path('logout/',views.LogOutApiView.as_view(),name="logout"),
    path('patient/active/<uid64>/<token>/',views.activation,name="activate"),
]