from django.urls import path
from course import views
urlpatterns = [
    path('getcor/',views.get_course1),
]
