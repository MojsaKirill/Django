from django.contrib import admin
from myapp.models import Person, Note

# Register your models here.

admin.site.register(Person)
admin.site.register(Note)