from django.urls import path
from .views import *

app = 'main'

urlpatterns = [
    path('', task_list, name='home'),
    path('task_create/', TaskCreateView.as_view(), name='task_create'),
]
