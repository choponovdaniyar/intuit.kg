from django.urls import  path, include
from . import views


app_name = "main"

urlpatterns = [
    path("", views.MainView.as_view(), name="main"),
    path("enrollee/", views.EnrolleeView.as_view(), name="enrollee"),
    path("selection-committee/", views.CommitteeView.as_view(), name="selection-committee"),
    path("history/", views.HistoryView.as_view(), name="history"),
    path("timetable/", views.TimetableView.as_view(), name="timetable"),
    path("live/", views.LiveView.as_view(), name="live"),
    path("honor/<slug:status>", views.HonorView.as_view(), name="honor"),
    path("contact", views.ContactView.as_view(), name="contact"),
    path("quality-advice", views.QualityAdvice.as_view(), name="quality-advice")
]



