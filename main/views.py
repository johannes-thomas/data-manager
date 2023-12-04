from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from datetime import datetime
from main.forms import *
from main.models import *

class ObjectListView(ListView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super(ObjectListView, self).get_context_data(**kwargs)
        return context

def input_data(request):
    object = request.path.split("/")[1]
    
    match object:
        case "publisher":
            form = PublisherForm(request.POST or None)
        case "journal":
            form = JournalForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            journal = form.save(commit=False)
            journal.date_created = datetime.now()
            journal.save()
            return redirect(object)
    else:
        model = form.save(commit=False)
        return render(request, "input_data.html", {"form": form, "name": type(model).__name__})
