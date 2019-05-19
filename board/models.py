from django.conf import settings
from django.db import models


class Column(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Task(models.Model):
    text = models.TextField()
    column = models.ForeignKey(Column, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
