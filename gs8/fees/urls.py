from django.urls import path
from fees import views
urlpatterns = [
   path('feecourse/',views.get_fees),

    
]