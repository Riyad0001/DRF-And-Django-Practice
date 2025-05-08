from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('add/',views.add,name="add"),
    path('addrec/',views.addrec,name="addrec"),
    path("delete/<int:id>/",views.delet,name="delete")
]
