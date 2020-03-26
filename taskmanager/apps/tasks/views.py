from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view

from .models import Task
from .serializers import TaskSerializer


class TaskListView(generics.ListAPIView):
    """
        View that gets all tasks
    """
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
        View that get task detail
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TaskCreateView(generics.CreateAPIView):
    """
        View that creates a task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)