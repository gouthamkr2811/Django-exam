from web import views
from django.urls import path


app_name = "web"


urlpatterns = [
    path('', views.index, name="index"),
]