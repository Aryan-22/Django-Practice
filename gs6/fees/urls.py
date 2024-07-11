from django.contrib import admin
from django.urls import path
from fees import views
urlpatterns = [
    path('feesg/',views.g),

]