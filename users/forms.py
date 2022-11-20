from django import forms
from django.contrib.auth.models import User
from users.models import ToDo


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password"]

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['creat_task',]

        widgets = {
            'creat_task': forms.TextInput(attrs={'class': ' task'})
        
        }
