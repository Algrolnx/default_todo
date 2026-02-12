from django.shortcuts import render, redirect
from .models import Task, TaskHistory


def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        priority = request.POST.get('priority')
        category = request.POST.get('category')

        if title:
            Task.objects.create(
                title=title,
                priority=priority,
                category=category
            )
            TaskHistory.objects.create(task_title=title, action='created')
        return redirect('tasks:index')

    tasks = Task.objects.all()

    total_tasks = tasks.count()
    completed_tasks = tasks.filter(complete=True).count()
    progress = 0
    if total_tasks > 0:
        progress = int((completed_tasks / total_tasks) * 100)

    context = {
        'tasks': tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'progress': progress,
    }

    return render(request, 'tasks/index.html', context)


def del_task(request, pk):
    task = Task.objects.get(id=pk)
    TaskHistory.objects.create(task_title=task.title, action='deleted')
    task.delete()
    return redirect('tasks:index')


def toggle_task(request, pk):
    task = Task.objects.get(id=pk)
    task.complete = not task.complete
    task.save()

    action = 'completed' if task.complete else 'uncompleted'
    TaskHistory.objects.create(task_title=task.title, action=action)
    return redirect('tasks:index')


def history(request):
    entries = TaskHistory.objects.all()[:50]
    return render(request, 'tasks/history.html', {'entries': entries})
