from django.forms import models
from .models import Task


class TaskAddForm(models.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
