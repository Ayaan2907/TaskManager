from django.db import models
from django.utils import timezone

# table for storing boards
class List_board(models.Model):
  name = models.CharField(max_length=50)
  created_at = models.DateTimeField(default=timezone.now)
  def __str__(self):
        return f"{self.name}"

# table for storing lists
class Task_list(models.Model):
  name = models.CharField(max_length=50)
  note = models.TextField()
  created_at = models.DateTimeField(default=timezone.now())
  board_key = models.ForeignKey(List_board, on_delete= models.CASCADE)
  def __str__(self):
    return f"{self.name}"

# table for storing tasks
class Task(models.Model):
  name = models.CharField(max_length=50)
  desc = models.TextField()
  created_at = models.DateTimeField(default=timezone.now())
  due_date = models.DateTimeField()
  list_key = models.ForeignKey(Task_list, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.name}"