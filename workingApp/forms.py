from django import forms
from workingApp.models import *

# form to get list data 
class Task_list_form(forms.Form):
  # name = forms.CharField(max_length=50)
  # note = forms.TextInput()
  # # created_at = forms.DateTimeField(default=timezone.now())
  # # created_at = forms.DateTimeInput()
  # # board_key = forms.InlineForeignKeyField(board_key)

#  FIXME: meta method is not working look into it till then all fields are manually inserted here
  class Meta:
    model = Task_list
    fields = '__all__'


# form to get task data 
class Task_form(forms.Form):
  # name = forms.CharField(max_length=50)
  # desc = forms.TextInput()
  # # created_at = forms.DateTimeInput()
  # due_date = forms.DateTimeInput()
  # # list_key = forms.InlineForeignKeyField(Task_list)



# FIXME: meta method is not working look into it till then all fields are manually inserted here
  class Meta:
    model = Task
    fields = '__all__'
    widgets = {
      'due_date': forms.DateTimeInput(attrs= {'type': 'datetime-local'})
    }
