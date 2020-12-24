from django import forms

class AddTaskForm(forms.Form):
    newTask = forms.CharField(label="Add Task")
