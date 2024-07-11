from django.urls import path
from fees import views
urlpatterns = [
    path('getfe/',views.getfees)

]
