from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
    
class Lists(models.Model):
    title = models.CharField(max_length = 20)
    time_stamp = models.DateTimeField(default=timezone.now())
    note = models.TextField(max_length= 200)
    def __str__(self):
        return(f"{self.title}")


class Task(models.Model):
    name = models.CharField(max_length = 20)
    task_description = models.TextField(max_length= 200)
    time_stamp = models.DateTimeField(default=timezone.now())
    due_date = models.DateTimeField()
    list_key = models.ForeignKey(Lists, on_delete=models.CASCADE)
    def __str__(self):
        return(f"{self.name}")