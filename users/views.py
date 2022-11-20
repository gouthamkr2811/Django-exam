
import json

from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from posts.models import Author
from users.models import ToDo
from users.forms import ToDoForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect




from users.forms import UserForm
from main.functions import generate_form_errors

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)

                return HttpResponseRedirect("/")

        context = {
            "title": "Login",
            "error": True,
            "message": "Invalid username or password"
        }
        return render(request, "users/login.html", context)
    else:
        context = {
            "title": "Login",

        }
        return render(request, "users/login.html", context)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("web:index"))


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)

            user= User.objects.create_user(
                    first_name=instance.first_name,
                    last_name=instance.last_name,
                    email=instance.email,
                    password=instance.password,
                    username=instance.username
                )
            Author.objects.create(
                    name=instance.first_name,
                    user=user
                )

            user = authenticate(
                request, username=instance.username, password=instance.password)
            auth_login(request, user)

            return HttpResponseRedirect(reverse('web:index'))
        else:
            message = generate_form_errors(form)
            form = UserForm()
            context = {
                "title": "Signup",
                "error": True,
                "form": form,
                "message": message
            }
            return render(request, "users/create.html", context)
    else:
        form = UserForm()
        context = {
            'title': "Signup",
            "form": form,
        }
        return render(request, "users/create.html", context=context)


@login_required
def create_task(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.username = request.user
            instance.save()

            return HttpResponseRedirect(reverse('web:index'))
    else:
         form = ToDoForm()
         instances = ToDo.objects.filter(is_deleted=False)    
         context = {
                "title" : "Home Page",
                "instances": instances,
                "message" : generate_form_errors(form),
                "form":form
            }
         return render(request, 'users/web/index.html', context=context)
            
        

        
@login_required
def view_task(request):
    instance = ToDo.objects.filter(is_deleted=False)

    context = {
        "instance": instance
    }

    return render(request, "website/event/view_event.html", context)


@login_required
def delete_task(request, id):
    enquiry = get_object_or_404(ToDo, id=id)
    enquiry. is_deleted=True
    enquiry.delete()
    context={}
    # return render(request, "users/web/index.html", context=context)
    return HttpResponseRedirect(reverse('web:index'))



@login_required
def edit_task(request, id):
     instance = get_object_or_404(ToDo, id=id)
     if request.method == 'POST':
        form = ToDoForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

     else:
        form = ToDoForm(instance=instance)
        context={
            "form":form
        }
        return render(request, "users/web/index.html", context=context)


def completed_task(request,id ):
     enquiry = get_object_or_404(ToDo, id=id)
     enquiry.completed_task=True
     enquiry.save()
     return HttpResponseRedirect(reverse('web:index'))
