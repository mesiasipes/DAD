# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from todos.models import Item

from django.contrib.auth.decorators import login_required

from todos.forms import ToDoItemForm


@login_required
def todos(request):
    if request.method == "POST":
        item_id = request.POST.get('id')
        # TODO: check that Item is owned by User
        # TODO: handle a case of a user passing a bad 'id'
        # hint: Item does not exist
        obj = Item.objects.get(id=item_id)
        obj.completed = True
        obj.save()
    context = {
        'all_of_them': Item.objects.filter(user=request.user)
    }
    return render(request, 'todos.html', context)


@login_required
def new_todo(request):
    form = ToDoItemForm()
    if request.method == 'POST':
        form = ToDoItemForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
    context = {
        'form': form,
    }
    return render(request, 'new_todo.html', context)