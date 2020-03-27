from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def get_absolute_url(self):
        return reverse("task-detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.title
    
