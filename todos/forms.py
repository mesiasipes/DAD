from django import forms

from todos.models import Item

class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'text', 'priority', ]


class CompleteToDoItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['id', ]