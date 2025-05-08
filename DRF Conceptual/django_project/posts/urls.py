from django.contrib import admin
from django.urls import path,include
from .views import PostList,PostDetails
urlpatterns = [
    path('',PostList.as_view(),name="post_list"),
    path('<int:pk>/',PostDetails.as_view(),name="post_details"),
    
]