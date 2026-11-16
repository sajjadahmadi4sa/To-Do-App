from django.test import TestCase
from django.urls import reverse
from accounts.models import User
from tasks.models import Task


class TaskCRUDTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="user@test.com",password="Password123!")
        self.client.force_login(self.user)
        self.task = Task.objects.create(author=self.user,title="Test Task")

    def test_create_task_successfully(self):
        response = self.client.post(
            reverse("tasks:create_task"),{"title": "New Task"})

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(author=self.user,title="New Task").exists())

    def test_delete_task_successfully(self):
        response = self.client.post(reverse("tasks:delete_task", args=[self.task.id]))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    def test_update_task_successfully(self):
        response = self.client.post(
            reverse("tasks:edit_task", args=[self.task.id]),
            {"title": "Updated Task"})
        self.task.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.task.title, "Updated Task")

    def test_done_task_successfully(self):
        response = self.client.post(reverse("tasks:done_task", args=[self.task.id]))
        self.task.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.task.status)