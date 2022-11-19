from django.contrib import admin
from users.models import ToDo

# Register your models here.
class AdminToDo(admin.ModelAdmin):
    list_display =["id", "creat_task","pk"]

admin.site.register(ToDo,AdminToDo)
