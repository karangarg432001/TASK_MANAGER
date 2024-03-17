from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Task

class AuthenticationAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()

    def test_user_login(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post('/login/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.task = Task.objects.create(
            title='Test Task',
            description='This is a test task',
            completed=False,
            user=self.user
        )

    def test_create_task(self):
        self.client.force_authenticate(user=self.user)
        data = {'title': 'Test Task', 'description': 'This is a test task in test_create_task','user': self.user.id}
        response = self.client.post('/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_list_tasks(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_retrieve_task(self):
        response = self.client.get(f'/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')
    
    def test_update_task(self):
        data = {
            'title': 'Updated Task',
            'description': 'This is an updated task',
            'completed': True,
            'user': self.user.id
        }
        response = self.client.put(f'/tasks/{self.task.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Task')
        self.assertEqual(response.data['completed'], True)
    
    def test_partial_update_task(self):
        data = {
            'completed': True
        }
        response = self.client.patch(f'/tasks/{self.task.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['completed'])
    
    def test_delete_task(self):
        response = self.client.delete(f'/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())
