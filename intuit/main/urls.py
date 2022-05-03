from xml.etree.ElementInclude import include
from django.urls import  path, include
from . import views


app_name = "main"

urlpatterns = [
    path("", views.main, name="main"),
    path("enrollee/", views.enrollee, name="enrollee")
]



