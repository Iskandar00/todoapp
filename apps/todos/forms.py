from django import forms

from apps.todos.models import Todo


class TodosForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
