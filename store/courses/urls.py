from django.urls import path, include
from .views import CoursesListView

urlpatterns = [
    path('courses/all', CoursesListView.as_view()),
]
