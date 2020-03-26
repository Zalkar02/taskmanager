from django.db import models

from apps.tasks.models import Task


class Tag(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    tasks = models.ManyToManyField(Task, related_name='tags')

    def __str__(self):
        return self.name
    