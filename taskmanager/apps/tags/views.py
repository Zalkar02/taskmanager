from rest_framework import generics
from rest_framework.decorators import api_view

from .models import Tag
from .serializers import TagSerializer


class TagListView(generics.ListAPIView):
    """
        View that gets all Tags
    """
    queryset = Tag.objects.all().order_by('-id')
    serializer_class = TagSerializer
    

class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
        View that get Tag detail
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagCreateView(generics.CreateAPIView):
    """
        View that creates a Tag
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer