from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from myapp.models import Note
from .forms import RegistrationForm, LoginForm


# Create your views here.

def index(request):
    current_user = request.user
    notes = Note.objects.all().filter(user_id=current_user.id)
    return render(request, "index.html", {"notes": notes, "user": request.user})

def register(request):
    form = RegistrationForm()

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        try:
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("/")
        except IndentationError:
            return render(request, "registration/register.html", {"form": form, "error": "Такой логин уже существует"})
        except:
            return render(request, "registration/register.html", {"form": form, "error": "Ошибка"})
    else:
        return render(request, "registration/register.html", {"form": form})


@login_required
def editNote(request, id):
    note = Note.objects.get(id=id)
    if request.method == "POST":
        note.title = request.POST.get("title")
        note.description = request.POST.get("description")
        note.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "edit.html", {"note": note})


@login_required
def deleteNote(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return HttpResponseRedirect("/")


@login_required
def addNote(request):
    if request.method == "POST":
        current_user = request.user
        title = request.POST.get("title")
        description = request.POST.get("description")
        user_id = current_user.id
        note = Note.objects.create(title=title, description=description, user_id=user_id)
        return HttpResponseRedirect("/")
    else:
        return render(request, "add.html")
