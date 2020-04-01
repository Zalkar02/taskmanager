from rest_framework import serializers
from apps.users.serializers import UserSerializer
from .models import Task



class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('url','title', 'description', 'status', 'created', 'user', 'tags')clear
        