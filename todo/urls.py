from django.urls import path

from .views import addTask, mark_as_done

urlpatterns = [
    path('addTask', addTask, name='add-task'),
    path('mark_as_done/<int:pk>/', mark_as_done, name='mark-as-done'),
]