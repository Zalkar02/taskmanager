from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view

from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner


class TaskListView(generics.ListAPIView):
    """
        View that gets all tasks
    """
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        # self.request.user.tasks.all()
        return Task.objects.filter(user=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
        View that get task detail
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)


class TaskCreateView(generics.CreateAPIView):
    """
        View that creates a task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
