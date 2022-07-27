from django.urls import path 
from . import views
from .views import (
    TaskListView, 
    TaskCreateView, 
    TaskUpdateView, 
    TaskDeleteView, 
    HabitsListView, 
    HabitCreateView,
    HabitDeleteView,
)

urlpatterns = [
    path('habits/', HabitsListView.as_view(), name='habits'),
    path('new-habit/', HabitCreateView.as_view(), name='new-habit'),
    path('habits/<int:pk>/habit-delete/', HabitDeleteView.as_view(), name='delete-habit'),

    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
    path('task/<int:pk>', TaskUpdateView.as_view(), name='update'),
    path('new-task/', TaskCreateView.as_view(), name='new-task'),

    path('about-us/', views.about, name='about'),
    path('', TaskListView.as_view(), name='front'),
]