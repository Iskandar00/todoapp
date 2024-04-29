from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, DetailView

from apps.todos.models import Todo
from apps.todos.forms import TodosForm


def todo(request):
    todos = Todo.objects.all().order_by('-id')
    context = {
        'todos': todos
    }

    return render(request, 'todo_list.html', context)


def todo_add(request):
    form = TodosForm()
    context = {
        'form': form
    }
    return render(request, 'todo_add.html', context)


def todo_create(request):
    if request.method != 'POST':
        return redirect('todo_add-page')
    data = request.POST
    form = TodosForm(data=data)
    if form.is_valid():
        messages.info(request, 'successfully')
        form.save()
        return redirect('todo-page')
    else:
        messages.error(request, form.errors)
        return redirect('todo-page')


class DeleteViewPage(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('todo-page')


class UpdateViewPage(UpdateView):
    model = Todo
    template_name = 'update.html'
    success_url = reverse_lazy('todo-page')
    form_class = TodosForm


class DetailViewPage(DetailView):
    model = Todo
    template_name = 'detail.html'
    success_url = reverse_lazy('todo-page')
    form_class = TodosForm

