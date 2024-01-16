from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import TaskCreateForm
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, "task_list.html", context)


def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    context = {
        'task': task
    }
    return render(request, "task_detail.html", context)


class TaskCreateView(View):

    def get(self, request):
        form = TaskCreateForm()
        context = {
            "add_form": form
        }
        return render(request, "task_create.html", context)

    def post(self, request):
        form = TaskCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
        context = {
            "add_form": form
        }
        return render(request, "task_create.html", context)


class TaskUpdateView(View):

    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        form = TaskCreateForm(instance=task)
        context = {
            "update_form": form
        }
        return render(request, "task_update.html", context)

    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)
        form = TaskCreateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")
        context = {
            "update_form": form
        }
        return render(request, "task_update.html", context)


def task_status_update(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_complete = not task.is_complete
    task.save()
    return redirect("home")


def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("home")
