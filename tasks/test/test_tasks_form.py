from django.test import TestCase
from tasks.forms import TaskForm


class TaskFormTest(TestCase):

    def test_task_form_with_valid_data(self):
        form = TaskForm(data={"title": "Test Task","description": "Test Description"})
        self.assertTrue(form.is_valid())

    def test_task_form_with_invalid_data(self):
        form = TaskForm(data={"title": "","description": "Test Description"})
        self.assertFalse(form.is_valid())