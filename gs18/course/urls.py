from django.urls import path
from course import views

urlpatterns = [
    path('djangooo/',views.learn_django,name = "courseone")
]
