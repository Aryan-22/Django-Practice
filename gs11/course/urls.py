from django.urls import path
from course import views
urlpatterns = [
   path('gc1/',views.getcourse1),
   path('gc2/',views.getcourse2)
]