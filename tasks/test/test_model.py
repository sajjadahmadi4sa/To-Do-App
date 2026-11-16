from django.test import TestCase
from accounts.models import User
from tasks.models import Task


class TaskModelTest(TestCase):

    def test_create_task(self):
        user = User.objects.create_user(email="user@test.com",password="Password123!")
        task = Task.objects.create(author=user,title="Test Task")

        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.author, user)
        self.assertFalse(task.status)