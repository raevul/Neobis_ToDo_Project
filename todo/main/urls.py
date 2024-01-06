from django.urls import path
from .views import *

urlpatterns = [
    path('', task_list, name='home'),
    path('task_create/', TaskCreateView.as_view(), name='task_create'),
    path('task_update/<int:task_id>/', TaskUpdateView.as_view(), name="task_update"),
    path('task_status_update/<int:task_id>/', task_status_update, name='task_status_update'),
    path('task_delete/<int:task_id>/', task_delete, name="task_delete"),
]
