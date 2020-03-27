
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Task


class TaskTest(APITestCase):
    def setUp(self):
        user = User.objects.create(username='testuser', email='test@mail.com')
        user.set_password('testpassword')
        user.save()
        Task.objects.create(title = 'Test Title', description='some descr', user=user, status=False)

    def test_get_task_list(self):
        """
            Test to get all tasks
        """
        url = reverse('task-list')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_task_detail(self):
        """
            Test to get task by id
        """
        task = Task.objects.first()
        url = task.get_absolute_url()
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_task(self):
        """
            Test to create task
        """
        url = reverse('task-create')  #http://localhost:8000/api/tasks/create

        self.client.login(username='testuser', password='testpassword')
        data = {'title': 'some title', 'description': 'some test'}
        
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.get(title='some title').title, 'some title')