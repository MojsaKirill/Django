from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import logout

from myapp.models import Person
from .forms import UserForm, RegistrationForm


# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        Person.objects.create(name=name, age=age)
        return HttpResponseRedirect("/")
    else:
        userform = UserForm()
        people = Person.objects.all()
        return render(request, "index.html", {"form": userform, "peoples": people, "user": request.user.username})

def editPerson(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def deletePerson(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def register(request):
    form = RegistrationForm()

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)
        user.password.encode()
        user.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "registration/register.html", {"form" : form})

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect("/")
