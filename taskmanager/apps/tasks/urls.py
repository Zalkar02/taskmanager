from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename='task')


urlpatterns = [
    path('done_tasks/', views.TaskViewSet.as_view({'get': 'get_done_tasks'}), name='done-tasks')
]


urlpatterns += router.urls