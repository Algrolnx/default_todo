from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task, TaskHistory
from .serializers import TaskSerializer, TaskHistorySerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        TaskHistory.objects.create(task_title=task.title, action='created')

    def perform_destroy(self, instance):
        TaskHistory.objects.create(task_title=instance.title, action='deleted')
        instance.delete()

    @action(detail=True, methods=['post'])
    def toggle(self, request, pk=None):
        task = self.get_object()
        task.complete = not task.complete
        task.save()

        action_name = 'completed' if task.complete else 'uncompleted'
        TaskHistory.objects.create(task_title=task.title, action=action_name)

        return Response({'status': 'toggled', 'complete': task.complete})

    @action(detail=False, methods=['get'])
    def stats(self, request):
        total_tasks = self.get_queryset().count()
        completed_tasks = self.get_queryset().filter(complete=True).count()

        progress = 0
        if total_tasks > 0:
            progress = int((completed_tasks / total_tasks) * 100)

        return Response({
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'progress': progress,
        })


class TaskHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TaskHistory.objects.all()[:50]
    serializer_class = TaskHistorySerializer
