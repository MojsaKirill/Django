from django.contrib import admin
from myapp.models import Person, Note
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Person)
admin.site.register(Note)