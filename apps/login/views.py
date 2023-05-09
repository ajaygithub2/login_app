from django.shortcuts import render, redirect
from .models import Users, Tasks
from .forms import CreateAccountForm, FormLogin, AddTaskForm
from django.contrib import messages
from django.urls import reverse
import datetime
from django.db.models import Q

def index(request):
    if request.method == "GET":
        return render(request, "login/index.html", {"form": FormLogin()})

    elif request.method == "POST":
        form = FormLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"].lower()
            password = form.cleaned_data["password"]
            try:
                obj = Users.objects.all().filter(Q(username=username) | Q(email=username)).first()
            except:
                pass
            if obj and (password == obj.password):
                request.session["username"] = obj.username
                return redirect("login:session")
            else:
                return render(
                    request, "login/index.html", {"form": form, "error": "error"}
                )
    

def create_account(request):
    if request.method == "GET":
        form = CreateAccountForm()
        return render(request, "login/create_account.html", {"form": form})
    
    elif request.method == "POST":
        form = CreateAccountForm(request.POST)
        text = ""
        if form.is_valid():
            first_name = form.cleaned_data["first_name"].capitalize()
            last_name = form.cleaned_data["last_name"].capitalize()
            email = form.cleaned_data["email"]
            new_username = form.cleaned_data["new_username"].lower()
            new_password = form.cleaned_data["new_password"]
            confirm_password = form.cleaned_data["confirm_password"]
            database = Users.objects.all()
            all_usernames = [i.username for i in database]
            all_emails = [i.email for i in database]
            if email in all_emails:
                text = "Email already used!"
            elif new_password != confirm_password:
                text = "Passwords don't match."
            elif new_username in all_usernames:
                text = "Username already exists! Please try a different username."
            elif new_username not in all_usernames and (new_password == confirm_password):
                obj = Users(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=new_username,
                    password=new_password,
                )
                obj.save()
                text = "Your account has been created."
                messages.success(request, ("Your account has been created successfully."))
                return redirect("login:index")
            return render(
                request, "login/create_account.html", {"form": form, "text": text}
            )
        else:
            return render(
                request, "login/create_account.html", {
                    "form": form, "text": text
                }
            )

def session(request):
    if request.method == "GET":
        user = Users.objects.filter(username=request.session["username"]).first()
        tasks = Tasks.objects.filter(user=user)
        return render(
            request, "login/session.html", {"user": user, "tasks": tasks, "add_task_form": AddTaskForm(), "curdate": datetime.date.today()}
        )

def add_task(request):
    if request.method == "POST":
        add_task_form = AddTaskForm(request.POST)
        if add_task_form.is_valid():
            new_task = add_task_form.cleaned_data["new_task"]
            finish_by = add_task_form.cleaned_data["finish_by"]
            user = Users.objects.get(username=request.session["username"])
            task = Tasks(user=user,finish_by= finish_by, task=new_task)
            task.save()
            return redirect(reverse("login:session"))
            
def delete_task(request, task_id):
    if request.method == "POST":
        task = Tasks.objects.filter(pk=task_id).first()
        task.delete()
        return redirect("login:session")

def logout(request):
    request.session.clear()
    request.session.flush()
    return redirect("login:index")
