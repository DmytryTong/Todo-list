from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    content = models.CharField(max_length=255)
    creation_time = models.DateTimeField()
    deadline = models.DateTimeField(null=True)
    complete = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")
