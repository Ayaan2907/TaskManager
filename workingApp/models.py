from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# table for storing lists
class Task_list(models.Model):
  name = models.CharField(max_length=50)
  note = models.TextField()
  user_key = models.ForeignKey(User, on_delete= models.CASCADE)#storing user_id
  created_at = models.DateTimeField(default=timezone.now) # if we write default = timezone.now() the timezone function gets called and it takes the time when the migrations are run. instead use timezone.now which gets called at the object creation
  def __str__(self):
    return f"{self.name}" 

# table for storing tasks
class Task(models.Model):
  name = models.CharField(max_length=50)
  desc = models.TextField()
  created_at = models.DateTimeField(default=timezone.now) # if we write default = timezone.now() the timezone function gets called and it takes the time when the migrations are run.  instead use timezone.now which gets called at the object creation
  # due_date = models.DateField() 
  list_key = models.ForeignKey(Task_list, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.name}"
