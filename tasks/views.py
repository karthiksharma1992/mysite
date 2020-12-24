from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import AddTaskForm
from django.urls import reverse

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            newTask = form.cleaned_data["newTask"]
            request.session["tasks"] += [newTask]
            return HttpResponseRedirect(reverse("tasks:index")) #check why this shit is not working.
        else:
            return render(request, 'tasks/index.html', {'form': form})
    context = {'tasks': request.session["tasks"], 'form': AddTaskForm()}
    return render(request, 'tasks/index.html', context)
