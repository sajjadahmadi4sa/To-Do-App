from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('create/', views.CreateTaskView.as_view(), name='create_task'),
    path('task_list/',views.ListTaskView.as_view(),name='task_list'),
    path('done/<int:pk>/', views.DoneTaskView.as_view(), name='done_task'),
    path('delete/<int:pk>/', views.DeleteTaskView.as_view(), name='delete_task'),
    path('edit/<int:pk>/', views.EditTaskView.as_view(), name='edit_task'),
]