from django.shortcuts import render
from rest_framework import generics

from .models import Task
from .serializers import TaskSerializer


#CRUD
class TaskListView(generics.ListAPIView):
    """
        View that gets all tasks
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer