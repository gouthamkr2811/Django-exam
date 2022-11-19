from django.shortcuts import render
from django.http.response import HttpResponse
from users.forms import ToDoForm
from users.models import ToDo


def index(request):
    instances = ToDo.objects.filter(is_deleted=False)
    form = ToDoForm()    
    context = {
        "title" : "Home Page",
        "instances": instances,
         "form": form,  
    }
    return render(request,'users/web/index.html',context=context)