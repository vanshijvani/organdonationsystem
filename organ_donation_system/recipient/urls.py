from django.contrib import admin
from django.urls import path
from recipient import views

urlpatterns = [
    path("", views.register_recipient, name='recipient')
]