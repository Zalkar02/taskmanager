from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response



@api_view(['GET'])
def api_root(request, format=None):

    response = Response({
        'tasks': reverse('task-list', request=request, format=format),
        'task-create': reverse('task-create', request=request, format=format),

        'tags': reverse('tag-list', request=request, format=format),
        'tag-create': reverse('tag-create', request=request, format=format),

        'sign-up': reverse('user-create', request=request, format=format)
    })
    return response
