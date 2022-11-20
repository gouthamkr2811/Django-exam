from django.urls import path
from users import views


app_name = "users"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("create-task/", views.create_task, name="create_task"),
    path("delete-task/<int:id>/", views.delete_task, name="delete_task"),
    path("edit-task/<int:id>/", views.edit_task, name="edit_task"),
    path("completed-task/<int:id>/", views.completed_task, name="completed_task"),

]
