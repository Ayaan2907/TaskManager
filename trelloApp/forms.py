from django import forms
from django.utils import timezone
from .models import *
# class List_form(forms.Form):
#     title = forms.CharField(max_length = 20)
#     time_stamp = forms.DateTimeField(default=timezone.now())
#     note = forms.TextField(max_length= 200)
#  i did this add list part using html forms now using django i am writing tasks

class Task_form_old(forms.Form):
    name = forms.CharField(label='Your name')#,max_length = 20)
    task_description = forms.CharField( widget= forms.Textarea , label='Your name')
    due_date = forms.DateTimeField()

class Task_form(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {'due_date': forms.DateTimeInput(attrs={"type":"datetime-local"})}
        #  the above line is providing a right look to date time feild