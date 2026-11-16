from django.test import TestCase
from django.urls import reverse, resolve
from tasks.views import (
    CreateTaskView,
    ListTaskView,
    DoneTaskView,
    DeleteTaskView,
    EditTaskView
)


class TaskUrlTest(TestCase):

    def test_create_task_url_resolve(self):
        url = reverse('tasks:create_task')
        self.assertEqual(resolve(url).func.view_class, CreateTaskView)

    def test_task_list_url_resolve(self):
        url = reverse('tasks:task_list')
        self.assertEqual(resolve(url).func.view_class, ListTaskView)

    def test_done_task_url_resolve(self):
        url = reverse('tasks:done_task', args=[1])
        self.assertEqual(resolve(url).func.view_class, DoneTaskView)

    def test_delete_task_url_resolve(self):
        url = reverse('tasks:delete_task', args=[1])
        self.assertEqual(resolve(url).func.view_class, DeleteTaskView)

    def test_edit_task_url_resolve(self):
        url = reverse('tasks:edit_task', args=[1])
        self.assertEqual(resolve(url).func.view_class, EditTaskView)