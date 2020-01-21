from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Blog App Page"),
    path("post/", views.post, name="post"),
]
