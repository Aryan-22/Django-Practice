from django.urls import path
from course import views
urlpatterns = [
   path('getcourse/',views.get_course),

    
]