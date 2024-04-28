from django.shortcuts import render

from todo.models import Task

def home(request):
	tasks = Task.objects.filter(is_complete=False).order_by('-updated_at')
	comp_tasks = Task.objects.filter(is_complete=True)
	context = {
        'tasks': tasks,
		'comp_tasks': comp_tasks,
    }
	return render(request, 'home.html', context)