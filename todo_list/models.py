from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    creation_time = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(blank=True, null=True)
    complete = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        return f" Task: {self.content}"
