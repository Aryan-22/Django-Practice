from django.urls import path
from . import views
urlpatterns = [
    path('<int:my_id>/',views.show_details,name="details"),
    path('<int:my_id>/<int:my_subid>/',views.show_subdetails,name="subdetail"),

]
