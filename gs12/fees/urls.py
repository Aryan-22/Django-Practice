from django.urls import path
from fees import views
urlpatterns = [
    path('gf/',views.getfees),
]
