from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('post-data/', views.StudentViews.as_view()),
    path('post-data/<int:id>', views.StudentViews.as_view())
]
