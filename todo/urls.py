from django.urls import path

from .views import addTask, mark_as_done, delete_task, edit_task

urlpatterns = [
    path('addTask', addTask, name='add-task'),
    path('mark_as_done/<int:pk>/', mark_as_done, name='mark-as-done'),
    path('delete_task/<int:pk>/', delete_task, name='delete-task'),
    path('edit_task/<int:pk>/', edit_task, name='edit-task'),
]