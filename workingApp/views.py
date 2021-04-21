from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import *
from .models import *


class dashboard(LoginRequiredMixin, ListView):
    model = TaskList
    context_object_name = 'lists' # this is used as providing the context in template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = context['lists'].filter(userKey=self.request.user)
#         context['count'] = context``['lists'].filter(complete=False).count()

#         search_input = self.request.GET.get('search-area') or ''
#         if search_input:
#             context['lists'] = context['lists'].filter(
#                 title__startswith=search_input)

#         context['search_input'] = search_input

        return context


class createList(LoginRequiredMixin, CreateView):
    model = TaskList
    fields = ['name']
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.userKey = self.request.user
        return super(createList, self).form_valid(form)

class createTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'desc', 'listKey','completionStatus']
    success_url = reverse_lazy('list_descr(request, listId)')

    def form_valid(self, form):
        # form.instance.listKey = self.kwargs.get('listId')
        return super(createTask, self).form_valid(form)

    #FIXME: 1>> success_url = redirect('list_desc', 'listId')
    #FIXME: 2>> listKey



# @login_required(login_url='signin')
# def create_task_form(request, list_id):
#     # get data from form and assign it
#     if request.method == 'POST':
#         form = Task_form(data=request.POST)
#         name = request.POST['name']
#         if form.is_valid():
#             form.save()
#             return redirect('list_descr', list_id)
#     else:
#         form = Task_form(initial= {'list_key': list_id})
#     return render(request,'workingApp/createTask.html', {'form':form})

@login_required(login_url='signin')
def list_descr(request, listId):
    lists = TaskList.objects.filter(id=listId)
    tasks = Task.objects.filter(listKey=listId)
    return render(request, 'workingApp/lists.html', {'tasks': tasks, 'list_name': lists[0].name, 'listId': lists[0].id})

