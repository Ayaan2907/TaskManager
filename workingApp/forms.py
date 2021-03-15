from django import forms
from workingApp.models import *
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
# form to get list data 
class Task_list_form(forms.ModelForm):
  # name = forms.CharField(max_length=50)
  # note = forms.TextInput()
  # # created_at = forms.DateTimeField(default=timezone.now())
  # # created_at = forms.DateTimeInput()
  # # board_key = forms.InlineForeignKeyField(board_key)

#  FIXME: FIXED : in line 5 and 19 forms.ModelForm earlier i was doing forms.Form
  class Meta:
    model = Task_list
    # fields = '__all__'
    fields = ['name', 'note', 'board_key']



# form to get task data 
class Task_form(forms.ModelForm):
  class Meta:
    model = Task
    # fields = '__all__'
    fields = ['name', 'desc', 'due_date', 'list_key']
    widgets = {'due_date': forms.DateTimeInput(attrs= {'type': 'datetime-local'})} 
    widgets = {
      'due_date': forms.DateTimeInput(attrs= {'type': 'datetime-local'})
    }