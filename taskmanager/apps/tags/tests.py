from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Task, Tag


class TagTest(APITestCase):
    def setUp(self):
        user = User.objects.create(username='testuser', email='test@mail.com')
        user.set_password('testpassword')
        user.save()
        Tag.objects.create(name='Test name')
        Task.objects.create(title = 'Test Title', description='some descr', user=user, status=False)

    def test_get_tag_list(self):
        """
            Test to get all tags
        """
        url = reverse('tag-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_tag_detail(self):
        """
            Test to get task by id
        """
        url = reverse('tag-detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test name')


    def test_create_tag(self):
        """
            Test to create tag
        """
        url = reverse('tag-create')
        data = {'name': 'Some name', 'tasks': ["http://127.0.0.1:8000/api/tasks/1/"]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Some name')


    def test_put_tag(self):
        """
            Test to put tag by id
        """
        url = reverse('tag-detail', kwargs={'pk': 1})
        data = {'name': 'Put name', 'tasks': ["http://127.0.0.1:8000/api/tasks/1/"]}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Put name')

    def test_delete_tag(self):
        """
            Test to delete tag by id
        """
        url = reverse('tag-detail', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)