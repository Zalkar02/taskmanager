from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner



class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['status', 'tags']

    def get_queryset(self):
        return self.request.user.tasks.all()


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    @action(detail=False, methods=['get'])
    def get_done_tasks(self, request):
        queryset = Task.objects.filter(status=True)
        serializer = TaskSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)