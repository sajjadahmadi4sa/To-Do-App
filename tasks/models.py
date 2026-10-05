from django.db import models
from accounts.models import User


class Task(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=450)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
# Create your models here.
