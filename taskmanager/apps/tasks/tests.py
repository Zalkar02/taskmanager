
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Task
from apps.tags.models import Tag


class TaskTest(APITestCase):
    def setUp(self):
        user = User.objects.create(username='testuser', email='test@mail.com')
        user.set_password('testpassword')
        user.save()
        Task.objects.create(title = 'Test Title', description='some descr', user=user, status=False)
        Tag.objects.create(name='python')

    def test_get_task_list(self):
        """
            Test to get all tasks
        """
        url = reverse('task-list') # http://localhost:8000/api/tasks/
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
        url = reverse('task-list')  #http://localhost:8000/api/tasks/

        self.client.login(username='testuser', password='testpassword')

        tag = Tag.objects.first()  # http://localhost:8000/api/tags/2/
        data = {'title': 'some title', 'description': 'some test', 'tags': [tag.get_absolute_url()] }
        
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.get(title='some title').title, 'some title')


    def test_put_task(self):
        """
            Test to put task by id
        """
        task = Task.objects.first()
        url = task.get_absolute_url()
        self.client.login(username='testuser', password='testpassword')
        data = {'title': 'Put title', "description": 'put test'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Put title')

    def test_delete_task(self):
        """
            Test to delete task by id
        """
        task = Task.objects.first()
        url = task.get_absolute_url()
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)