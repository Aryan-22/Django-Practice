from django.urls import path
from course import views

urlpatterns = [
    path('gc/', views.getcourse),
]

