from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
    path('', views.PostListView.as_view(), name="new_list"),
    path('<slug:category>/', views.PostCategoryListView.as_view(), name="new_category_list"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
            views.post_detail, name="new_detail")
]