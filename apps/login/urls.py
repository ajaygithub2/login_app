from django.urls import path
from . import views

app_name = "login"

urlpatterns = [
    path("", views.index, name="index"),
    path("session", views.session, name="session"),
    path("create_account", views.create_account, name="create_account"),
    path("<int:task_id>/delete_task", views.delete_task, name="delete_task"),
    path("add_task", views.add_task, name="add_task"),
]