"""
URL configuration for CrimsonCare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from donars.views import RegistrationView,LoginApiView,LogOutApiView,activation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('donar/',include("donars.urls")),
    path('req/',include("blood_request.urls")),
    path('register/',RegistrationView.as_view(),name="register"),
    path('login/',LoginApiView.as_view(),name="login"),
    path('logout/',LogOutApiView.as_view(),name="logout"),
    path('donar/active/<uid64>/<token>/',activation,name="active"),

]
