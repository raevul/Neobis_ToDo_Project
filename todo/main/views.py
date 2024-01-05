from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import TaskAddForm
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "task_list.html", {"tasks": tasks})


class TaskCreateView(View):

    def get(self, request):
        add_form = TaskAddForm()
        return render(request, "task_create.html", {"add_form": add_form})

    def post(self, request):
        form = TaskAddForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save()
            return redirect("home")
        return render(request, "task_create.html", {"add_form": form})


def task_detail(request):
    return render(request, "task_detail.html")
