from django.contrib import admin
from django.urls import path, include

from . import views
app_name = 'faculty'

urlpatterns = [
    path("faculties/", views.FacultiesFormView.as_view(), name="faculties"),
    path("collagies/", views.CollagiesFormView.as_view(), name="collage"),
    path('faculties/<slug:faculty>/', views.FacultyFormView.as_view(), name="faculty"),
    path('education/<slug:education>/', views.EducationListView.as_view(), name="education"),
    path('<slug:faculty>/<slug:education>/<slug:eduform>/<slug:title>', 
            views.ProfileListView.as_view(), name="profile")
]
