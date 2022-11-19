from django.urls import path
from users import views


app_name = "users"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("create-task/", views.create_task, name="create_task"),
    path("delete-task/", views.delete_task, name="delete_task"),

]
