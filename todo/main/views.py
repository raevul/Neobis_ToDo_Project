from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import TaskCreateForm
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "task_list.html", {"tasks": tasks})


class TaskCreateView(View):

    def get(self, request):
        add_form = TaskCreateForm()
        return render(request, "task_create.html", {"add_form": add_form})

    def post(self, request):
        form = TaskCreateForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save()
            return redirect("home")
        return render(request, "task_create.html", {"add_form": form})


class TaskUpdateView(View):

    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        form = TaskCreateForm(instance=task)
        return render(request, "task_update.html", {"update_form": form})

    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)
        form = TaskCreateForm(request.POST, instance=task)
        if form.is_valid():
            modified_task = form.save()
            return redirect("home")
        return render(request, "task_update.html", {"update_form": form})


def task_update_status(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_complete = not task.is_complete
    task.save()
    return redirect("home")


def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("home")
