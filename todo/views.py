from django.http import HttpResponse # type: ignore
from django.shortcuts import render, redirect, get_object_or_404 # type: ignore

from .models import Task

# Create your views here.
def addTask(request):
    if request.method == 'POST':
        task = request.POST['task']
        Task.objects.create(task=task)
        return redirect('home')
    else:
        return HttpResponse('Could not be saved')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_complete = True
    task.save()
    return redirect('home')

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        update = request.POST['task']
        task.task = update
        task.save()
        return redirect('home')
    else:
        context = {
            'task': task,
        }
    return render(request, 'edit_task.html', context)
