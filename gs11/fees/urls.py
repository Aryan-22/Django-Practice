from django.urls import path
from fees import views
urlpatterns = [
   path('gf1/',views.getfees1),
   path('gf2/',views.getfees2)
]