from django.shortcuts import render, HttpResponse

# Create your views here.
def addTask(request):
    return HttpResponse('Add Task')
